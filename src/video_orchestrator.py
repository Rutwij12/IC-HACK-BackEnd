from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List
from pydantic import BaseModel, Field
from .scene_planner import ScenePlanner
from .code_generator import CodeGenerator
from .llm_provider import LLMWrapper
import asyncio
from .prompts import (
    VIDEO_IDEA_GENERATOR_SYSTEM_PROMPT,
    VIDEO_IDEA_GENERATOR_USER_PROMPT
)

class SceneIdeas(BaseModel):
    scenes: List[str]

class VideoState(TypedDict):
    """Graph state for video orchestration"""
    video_prompt: str
    scene_ideas: List[str]
    scene_plans: List[str]
    scene_codes: List[str]
    final_code: str
    iterations: int

class VideoOrchestrator:
    def __init__(self, video_prompt: str, model: str = "claude-3-5-sonnet-20241022"):
        self.video_prompt = video_prompt
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
                f"{idea}"
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
                temp_file_prefix=f"scene_{idx}"
            )
            result = await generator.generate_code_with_feedback()
            return result["current_code"]
        
        # Create tasks for all scene codes
        tasks = [generate_single_scene(idx, plan) 
                for idx, plan in enumerate(state["scene_plans"])]
        # Run all tasks concurrently
        scene_codes = await asyncio.gather(*tasks)
        
        return {"scene_codes": scene_codes}

    def _combine_code(self, state: VideoState):
        """Combine all scene code into a single file and execute"""
        combined_code = """from manim import *

class CombinedScene(Scene):
    def construct(self):
"""
        # Add each scene's code as a subsection
        for idx, code in enumerate(state["scene_codes"]):
            # Extract the construct method content
            construct_content = code.split("def construct(self):")[1]
            # Indent the content
            indented_content = "\n".join(
                "        " + line for line in construct_content.split("\n")
            )
            combined_code += f"\n        # Scene {idx + 1}\n{indented_content}\n"
            
            # Add transition after each scene except the last one
            if idx < len(state["scene_codes"]) - 1:
                combined_code += """
        # Transition
        self.wait(0.5)  # Wait for a moment
        self.play(*[FadeOut(mob) for mob in self.mobjects])  # Clear everything from screen
        self.wait(0.5)  # Brief pause before next scene
"""

        # Write and execute combined file
        with open("combined_scenes.py", "w") as f:
            f.write(combined_code)

        # Execute the combined file
        namespace = {}
        exec(combined_code, namespace, namespace)

        return {"final_code": combined_code}

    def _setup_workflow(self):
        """Create and setup the workflow graph"""
        workflow = StateGraph(VideoState)
        
        workflow.add_node("generate_ideas", self._generate_scene_ideas)
        workflow.add_node("plan_scenes", self._plan_scenes)
        workflow.add_node("generate_code", self._generate_scene_code)
        workflow.add_node("combine_code", self._combine_code)

        # Sequential flow
        workflow.add_edge(START, "generate_ideas")
        workflow.add_edge("generate_ideas", "plan_scenes")
        workflow.add_edge("plan_scenes", "generate_code")
        workflow.add_edge("generate_code", "combine_code")
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
