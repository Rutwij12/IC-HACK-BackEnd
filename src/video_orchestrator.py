from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List
from pydantic import BaseModel, Field
from .scene_planner import ScenePlanner
from .code_generator import CodeGenerator
from .llm_provider import LLMWrapper
import asyncio
import subprocess
import aiofiles
import re
import os
from .prompts import (
    VIDEO_IDEA_GENERATOR_SYSTEM_PROMPT,
    VIDEO_IDEA_GENERATOR_USER_PROMPT,
    VOICEOVER_GENERATOR_SYSTEM_PROMPT,
    VOICEOVER_GENERATOR_USER_PROMPT,
    COMBINATION_STEP_SYSTEM_PROMPT,
    COMBINATION_STEP_USER_PROMPT
)

class SceneIdeas(BaseModel):
    scenes: List[str]

class VideoState(TypedDict):
    """Graph state for video orchestration"""
    video_prompt: str
    scene_ideas: List[str]
    scene_plans: List[str]
    scene_codes: List[str]
    voiceover_scripts: List[str]
    final_code: str
    iterations: int

class VideoOrchestrator:
    def __init__(self, video_prompt: str, model: str = "claude-3-5-sonnet-20241022"):
        self.video_prompt = video_prompt
        self.llm = LLMWrapper(model=model)
        self.idea_generator = LLMWrapper(model=model).with_structured_output(SceneIdeas)
        self.workflow = self._setup_workflow()
        self.app = self.workflow.compile()

    def _generate_scene_ideas(self, state: VideoState):
        """Generate high-level scene ideas for the video"""
        messages = [
            ("system", VIDEO_IDEA_GENERATOR_SYSTEM_PROMPT),
            ("user", VIDEO_IDEA_GENERATOR_USER_PROMPT.format(video_prompt=state['video_prompt']))
        ]
        
        scene_ideas = self.idea_generator.invoke(messages)
        return {"scene_ideas": scene_ideas.scenes}

    async def _plan_scenes(self, state: VideoState):
        """Generate detailed plans for each scene idea asynchronously"""
        async def plan_single_scene(idea):
            print(f"single scene plan created")
            planner = ScenePlanner(
                f"{idea}",
                max_iterations=3
            )
            result = await planner.generate_scene_with_feedback()
            return result["current_plan"]
        
        # Create tasks for all scenes
        tasks = [plan_single_scene(idea) for idea in state["scene_ideas"]]
        # Run all tasks concurrently
        scene_plans = await asyncio.gather(*tasks)
        
        return {"scene_plans": scene_plans}

    async def _generate_scene_code(self, state: VideoState):
        """Generate code for each scene plan asynchronously"""
        async def generate_single_scene(idx, plan):
            print(f"single scene code index {idx} created")
            generator = CodeGenerator(
                plan,
                temp_file_prefix=f"scene_{idx}",
                max_iterations=8
            )
            result = await generator.generate_code_with_feedback()
            if "current_code" not in result:
                print(f"for some reason current code not in idx {idx}")
            return result["current_code"]
        
        # Create tasks for all scene codes
        tasks = [generate_single_scene(idx, plan) 
                for idx, plan in enumerate(state["scene_plans"])]
        # Run all tasks concurrently
        scene_codes = await asyncio.gather(*tasks)
        
        return {"scene_codes": scene_codes}

    async def _generate_voiceovers(self, state: VideoState):
        """Generate voiceover scripts for each scene asynchronously"""
        async def generate_single_voiceover(plan, code):
            messages = [
                ("system", VOICEOVER_GENERATOR_SYSTEM_PROMPT),
                ("user", VOICEOVER_GENERATOR_USER_PROMPT.format(
                    plan=plan,
                    code=code
                ))
            ]
            result = await self.llm.ainvoke(messages)
            print("result of voiceover: ", result)
            return result.content
        
        # Create tasks for all scenes
        tasks = [generate_single_voiceover(plan, code) 
                for plan, code in zip(state["scene_plans"], state["scene_codes"])]
        # Run all tasks concurrently
        voiceover_scripts = await asyncio.gather(*tasks)
        
        return {"voiceover_scripts": voiceover_scripts}

    async def _combine_code(self, state: VideoState):
        """Combine all scene codes into a single Manim script with voiceovers"""
        combined_code = [
            "from manim import *",
            "import random",
            "import numpy as np",
            "from manim_voiceover import VoiceoverScene",
            "from manim_voiceover.services.azure import AzureService",
            "",
            "class CombinedScene(VoiceoverScene):",
            "    def construct(self):",
            "        # Set up Azure TTS service",
            "        self.set_speech_service(AzureService(",
            "            voice='en-US-JennyNeural',",
            "            style='friendly'",
            "        ))",
            ""
        ]

        # For each scene and its voiceover
        for i, (scene_code, voiceover) in enumerate(zip(state["scene_codes"], state["voiceover_scripts"]), 1):
            # Add scene header comment
            combined_code.append(f"\n        # Scene {i}")
            
            # Add voiceover wrapper
            combined_code.append(f"        with self.voiceover(text=\"\"\"{voiceover.strip()}\"\"\") as tracker:")
            
            # Add transition between scenes
            if i != 0:
              combined_code.extend([
                  "",
                  "            # Transition",
                  "            self.wait(0.5)  # Wait for a moment",
                  "            self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen",
                  "            self.wait(0.5)  # Brief pause before next scene",
                  ""
              ])

            # Extract the content between the construct method definition and the end
            scene_lines = scene_code.split("\n")
            construct_start = False
            for line in scene_lines:
                if "def construct(self):" in line:
                    construct_start = True
                    continue
                if construct_start and line.strip():
                    print(f"line: {line}")
                    # Add only 8 spaces (2 levels) for scene content
                    combined_code.append(f"    {line}")

        combined_code.extend([
                  "",
                  "        # Transition",
                  "        self.wait(0.5)  # Wait for a moment",
                  "        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen",
                  "        self.wait(0.5)  # Brief pause before next scene",
                  ""
              ])

        # Join all lines with proper newlines
        final_code = "\n".join(combined_code)
        
        # Write the combined code to a file
        with open("combined_scenes.py", "w") as f:
            f.write(final_code)
        
        return {"final_code": final_code}
    
    # async def _combine_code(self, state: VideoState):
    #     """Combine all scene codes into a single Manim script with voiceovers using LLM"""
    #     # Format scenes and voiceovers with numbers
    #     print("voiceovers: ")
    #     print(state["voiceover_scripts"])
        
    #     numbered_scenes = [f"Scene {i+1}:\n{code}" for i, code in enumerate(state["scene_codes"])]
    #     numbered_voiceovers = [f"Voiceover {i+1}:\n{vo}" for i, vo in enumerate(state["voiceover_scripts"])]
        
    #     messages = [
    #         ("system", COMBINATION_STEP_SYSTEM_PROMPT),
    #         ("user", COMBINATION_STEP_USER_PROMPT.format(
    #             numbered_voiceovers="\n\n".join(numbered_voiceovers),
    #             numbered_scenes="\n\n".join(numbered_scenes)
    #         ))
    #     ]
        
    #     # Get combined code from LLM
    #     response = await self.llm.ainvoke(messages)
    #     response_content = response.content
    #     print("final response: ")
    #     print(response)
    #     # Extract code block from response
    #     import re
    #     code_blocks = re.findall(r'```python\n(.*?)```', response_content, re.DOTALL)
    #     final_code = code_blocks[-1] if code_blocks else response_content
        
    #     # Write the combined code to a file
    #     with open("combined_scenes.py", "w") as f:
    #         f.write(final_code)
        
    #     return {"final_code": final_code}

    def _setup_workflow(self):
        """Create and setup the workflow graph"""
        workflow = StateGraph(VideoState)
        
        workflow.add_node("generate_ideas", self._generate_scene_ideas)
        workflow.add_node("plan_scenes", self._plan_scenes)
        workflow.add_node("generate_code", self._generate_scene_code)
        workflow.add_node("generate_voiceovers", self._generate_voiceovers)
        workflow.add_node("combine_code", self._combine_code)

        # Sequential flow
        workflow.add_edge(START, "generate_ideas")
        workflow.add_edge("generate_ideas", "plan_scenes")
        workflow.add_edge("plan_scenes", "generate_code")
        workflow.add_edge("generate_code", "generate_voiceovers")
        workflow.add_edge("generate_voiceovers", "combine_code")
        workflow.add_edge("combine_code", END)

        return workflow

    async def orchestrate_video(self):
        """
        Orchestrate the entire video creation process asynchronously
        
        Returns:
            dict: Final state containing all intermediate and final results
        """
        initial_state = {
            "video_prompt": self.video_prompt,
            "iterations": 0
        }
        
        return await self.app.ainvoke(initial_state)

    async def generate_and_render_video(self) -> dict:
        """
        Orchestrate video creation and render the final video and thumbnail.
        
        Returns:
            dict: Contains paths to the rendered video and thumbnail
        """
        # First generate all the code and assets
        #result = await self.orchestrate_video()
        
        # Ensure the output directory exists
        os.makedirs("media", exist_ok=True)
        
        # Render the full video
        video_cmd = ["manim", "-pqm", "combined_scenes.py", "CombinedScene"]
        video_process = await asyncio.create_subprocess_exec(
            *video_cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await video_process.communicate()

        filename = "scene_1_temp_code.py"
        async with aiofiles.open(filename) as f:
                code_content = await f.read()

        # Extract the class name from the code
        class_match = re.search(r'class\s+(\w+)\s*\(', code_content)
        if not class_match:
            raise Exception("file for class regex not working")
        
        class_name = class_match.group(1)
        
        # Generate thumbnail by saving the last frame
        thumbnail_cmd = ["manim", "-s", "--format=png", filename, class_name]
        thumbnail_process = await asyncio.create_subprocess_exec(
            *thumbnail_cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await thumbnail_process.communicate()
        
        # Find the generated files
        video_path = None
        thumbnail_path = None
        
        for root, _, files in os.walk("media/videos"):
            for file in files:
                if file.endswith(".mp4"):
                    video_path = os.path.join(root, file)
                    break
        
        for root, _, files in os.walk("media/images"):
            for file in files:
                if file.endswith(".png"):
                    thumbnail_path = os.path.join(root, file)
                    break
        
        return {
            "video_path": "media/videos/combined_scenes/720p30/CombinedScene.mp4",
            "thumbnail_path": thumbnail_path,
        }
