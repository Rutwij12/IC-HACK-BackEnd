from langgraph.graph import StateGraph, START, END
from typing import TypedDict, List
from pydantic import BaseModel, Field
from llm_provider import LLMWrapper
import asyncio
from langchain_anthropic import ChatAnthropic
import os
import aiofiles
from prompts import (
    REACT_COMPONENT_PLANNER_SYSTEM_PROMPT,
    REACT_COMPONENT_PLANNER_USER_PROMPT,
    REACT_CODE_GENERATOR_SYSTEM_PROMPT,
    REACT_CODE_GENERATOR_USER_PROMPT,
)
import re


class ComponentIdeas(BaseModel):
    components: List[str]


class ReactState(TypedDict):
    """Graph state for React component orchestration"""
    component_prompt: str
    component_ideas: List[str]
    component_codes: List[str]
    final_code: str


class ReactOrchestrator:
    def __init__(self, component_prompt: str, model: str = "claude-3-5-sonnet-20241022"):
        self.component_prompt = component_prompt
        self.llm = ChatAnthropic(model=model, max_tokens_to_sample=2048)
        self.idea_generator = ChatAnthropic(
            model=model).with_structured_output(ComponentIdeas)
        self.workflow = self._setup_workflow()
        self.app = self.workflow.compile()

    async def _generate_component_ideas(self, state: ReactState):
        """Generate high-level component ideas"""
        messages = [
            ("system", REACT_COMPONENT_PLANNER_SYSTEM_PROMPT),
            ("user", REACT_COMPONENT_PLANNER_USER_PROMPT.format(
                user_prompt=state['component_prompt']
            ))
        ]

        component_ideas = self.idea_generator.invoke(messages)
        return {"component_ideas": component_ideas.components}

    async def _generate_component_code(self, state: ReactState):
        """Generate code for each component idea"""
        async def generate_single_component(idx, idea):
            messages = [
                ("system", REACT_CODE_GENERATOR_SYSTEM_PROMPT),
                ("user", REACT_CODE_GENERATOR_USER_PROMPT.format(
                    component_plan=idea
                ))
            ]
            result = await self.llm.ainvoke(messages)

            # Extract code blocks from the response
            code_blocks = []
            try:
                code_blocks = re.findall(
                    r'```jsx\n(.*?)```', result.content, re.DOTALL)
                if not code_blocks:
                    # Fallback to looking for any code blocks if tsx-specific ones aren't found
                    code_blocks = re.findall(
                        r'```(.*?)```', result.content, re.DOTALL)
            except Exception as e:
                print(f"Error extracting code blocks: {e}")
                print(f"Response content: {result.content}")
                return ""

            if not code_blocks:
                print(f"No code blocks found for component {idx + 1}")
                return ""

            code_to_save = code_blocks[-1].strip()

            # Save component to file
            component_path = f"Component{idx + 1}.tsx"
            async with aiofiles.open(component_path, "w") as f:
                await f.write(code_to_save)

            return code_to_save

        tasks = [generate_single_component(idx, idea)
                 for idx, idea in enumerate(state["component_ideas"])]
        component_codes = await asyncio.gather(*tasks)

        return {"component_codes": component_codes}

    async def _combine_components(self, state: ReactState):
        """Combine all components into a single React application"""
        # Extract component names using regex
        component_names = []
        for code in state["component_codes"]:
            # Look for either function or class component declarations
            match = re.search(r'(function|class)\s+(\w+)', code)
            if match:
                component_names.append(match.group(2))
            else:
                print(f"Warning: Could not extract component name from code: {
                      code[:100]}...")
                continue

        # Create base App.tsx content
        app_content = [
            """import React, {Component, PureComponent, Fragment, Children, createElement, cloneElement, createFactory, isValidElement, createContext, createRef, forwardRef, lazy, memo, useState, useEffect, useContext, useReducer, useCallback, useMemo, useRef} from 'react';""",
            "",
            # Include all component code directly
            *state["component_codes"],
            "",
            "function App() {",
            "  return (",
            "    <div>",
        ]

        # Stack all components vertically using their actual names
        for component_name in component_names:
            app_content.append(f"      <{component_name} />")
            app_content.append(
                # Add spacing
                "      <div style={{ marginBottom: '2rem' }} />")

        app_content.extend([
            "    </div>",
            "  );",
            "}",
            "",
            "export default App;",
        ])

        # Write App.tsx
        app_path = "App.tsx"
        async with aiofiles.open(app_path, "w") as f:
            await f.write("\n".join(app_content))

        return {"final_code": "\n".join(app_content)}

    def _setup_workflow(self):
        """Create and setup the workflow graph"""
        workflow = StateGraph(ReactState)

        workflow.add_node("generate_ideas", self._generate_component_ideas)
        workflow.add_node("generate_code", self._generate_component_code)
        workflow.add_node("combine_components", self._combine_components)

        # Sequential flow
        workflow.add_edge(START, "generate_ideas")
        workflow.add_edge("generate_ideas", "generate_code")
        workflow.add_edge("generate_code", "combine_components")
        workflow.add_edge("combine_components", END)

        return workflow

    async def orchestrate_components(self):
        """
        Orchestrate the entire React component creation process

        Returns:
            dict: Final state containing all intermediate and final results
        """
        initial_state = {
            "component_prompt": self.component_prompt
        }
        
        return await self.app.ainvoke(initial_state)

    async def generate_and_return_components(self) -> dict:
        """
        Orchestrate React component creation and return the final code.

        Returns:
            dict: Contains the final React code and individual component codes
        """
        # First generate all the components and combined code
        result = await self.orchestrate_components()

        # Ensure the output directory exists
        os.makedirs("components", exist_ok=True)

        return {
            "react_code": result["final_code"],
        } 
