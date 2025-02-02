from langgraph.graph import StateGraph, START, END
from typing import Annotated, TypedDict, List
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from llm_provider import LLMWrapper
from pydantic import BaseModel, Field
import asyncio
from prompts import (
    SCENE_PLANNER_SYSTEM_PROMPT,
    SCENE_EVALUATOR_SYSTEM_PROMPT,
    SCENE_PLAN_USER_PROMPT,
    SCENE_EVALUATION_USER_PROMPT
)


class SceneEvaluation(BaseModel):
    """Schema for scene plan evaluation results"""
    passes_criteria: bool = Field(
        description="Whether scene plan meets all criteria")
    feedback: str = Field(
        description="Feedback if plan fails criteria, empty if passes")


class State(TypedDict):
    """Graph state containing messages and evaluation results"""
    evaluation: SceneEvaluation
    iterations: int
    current_plan: str  # Store the latest plan for easy access


class ScenePlanner:
    def __init__(self, scene_prompt: str,
                 planner_model: str = "claude-3-5-sonnet-20241022",
                 evaluator_model: str = "claude-3-5-sonnet-20241022",
                 max_iterations: int = 1):
        """Initialize the ScenePlanner with two LLMs - one for planning and one for evaluation"""
        self.planner = LLMWrapper(model=planner_model)
        self.evaluator = LLMWrapper(
            model=evaluator_model).with_structured_output(SceneEvaluation)
        self.workflow = self._setup_workflow()
        self.app = self.workflow.compile()
        self.scene_prompt = scene_prompt
        self.max_iterations = max_iterations

    async def _generate_plan(self, state: State):
        """Generate scene plan based on prompt and any previous feedback"""
        messages = [
            ("system", SCENE_PLANNER_SYSTEM_PROMPT),
            ("user", SCENE_PLAN_USER_PROMPT.format(scene_prompt=self.scene_prompt))
        ]
        iterations = state["iterations"]
        current_plan = state["current_plan"]

        # If we have feedback from previous evaluation, add it
        if iterations > 0 and not state["evaluation"].passes_criteria and state["evaluation"].feedback:
            messages.append(("assistant", current_plan))
            messages.append(("user", f"Please revise the scene plan based on this feedback: {
                            state['evaluation'].feedback}"))

        response = await self.planner.ainvoke(messages)
        current_plan = response.content

        return {
            "iterations": iterations + 1,
            "current_plan": current_plan
        }

    async def _evaluate_plan(self, state: State):
        """Evaluate the generated scene plan using the evaluator LLM"""
        current_plan = state["current_plan"]

        # Create evaluation prompt
        eval_prompt = [
            ("system", SCENE_EVALUATOR_SYSTEM_PROMPT),
            ("user", SCENE_EVALUATION_USER_PROMPT.format(scene_plan=current_plan))
        ]

        # Get evaluation response
        evaluation = await self.evaluator.ainvoke(eval_prompt)
        print("evaluation::")
        print(evaluation)
        return {
            "evaluation": evaluation,
            "current_plan": current_plan
        }

    def _should_continue(self, state: State):
        """Determine whether to continue iteration"""
        if state["evaluation"].passes_criteria:
            print("---SCENE PLAN PASSED EVALUATION---")
            return "end"
        elif state["iterations"] >= self.max_iterations:  # Use max_iterations from instance
            print("---MAX ITERATIONS REACHED---")
            return "end"
        else:
            print("---CONTINUING TO NEXT ITERATION OF SCENE PLAN---")
            return "generate"

    def _setup_workflow(self):
        """Create and setup the workflow graph"""
        workflow = StateGraph(State)

        workflow.add_node("generate", self._generate_plan)
        workflow.add_node("evaluate", self._evaluate_plan)

        workflow.add_edge(START, "generate")
        workflow.add_edge("generate", "evaluate")
        workflow.add_conditional_edges(
            "evaluate",
            self._should_continue,
            {
                "generate": "generate",
                "end": END
            }
        )
        return workflow

    async def generate_scene_with_feedback(self):
        """
        Generate scene plan using the feedback loop graph.

        Returns:
            dict: Final state containing messages, evaluation results, and iterations
        """
        initial_state = {
            "iterations": 0,
            "current_plan": ""
        }

        return await self.app.ainvoke(initial_state)
