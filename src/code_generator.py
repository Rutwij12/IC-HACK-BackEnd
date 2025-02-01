from langgraph.graph import StateGraph, START, END
from typing import Annotated, TypedDict, List
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from .llm_provider import LLMWrapper
import os
import re
import asyncio
import aiofiles
from .prompts import CODE_GENERATOR_SYSTEM_PROMPT, CODE_GENERATOR_USER_PROMPT

# Structured output for code evaluation
class CodeEvaluation(BaseModel):
    """Schema for code evaluation results"""
    passes_criteria: bool = Field(description="Whether code meets all criteria")
    feedback: str = Field(description="Feedback if code fails criteria, empty if passes")

class State(TypedDict):
    """Graph state containing messages and evaluation results"""
    messages: List
    evaluation: CodeEvaluation
    iterations: int
    current_code: str

class CodeGenerator:
    def __init__(self, code_spec: str, temp_file_prefix="0", 
                 model: str = "claude-3-5-sonnet-20241022",
                 max_iterations: int = 5):
        """Initialize the CodeGenerator with LLM and workflow setup"""
        self.llm = LLMWrapper(model=model)
        self.workflow = self._setup_workflow()
        self.app = self.workflow.compile()
        self.code_spec = code_spec
        self.temp_file_prefix = temp_file_prefix
        self.max_iterations = max_iterations

    async def _generate_code(self, state: State):
        """Generate code based on prompt and any previous feedback"""
        messages = state["messages"]
        iterations = state["iterations"]
        
        response = await self.llm.ainvoke(messages)
        messages.append(("assistant", response.content))
        
        return {
            "messages": messages,
            "iterations": iterations + 1
        }

    async def _evaluate_code(self, state: State):
        """Evaluate generated code by writing to file and executing"""
        messages = state["messages"]
        # last_message = messages[-1][1]  # Get code from last assistant message
        last_message = messages[-1][1].content if hasattr(messages[-1][1], 'content') else messages[-1][1]

        # Extract code blocks between triple backticks
        try:
            code_blocks = re.findall(r'```python\n(.*?)```', last_message, re.DOTALL)
        except:
            print(last_message)
        
        if not code_blocks:
            # Fallback to looking for any code blocks if python-specific ones aren't found
            code_blocks = re.findall(r'```(.*?)```', last_message, re.DOTALL)
        
        if not code_blocks:
            return {
                "messages": messages,
                "evaluation": CodeEvaluation(
                    passes_criteria=False,
                    feedback="No code blocks found in the response"
                )
            }
        
        code_to_execute = code_blocks[-1].strip()
        filename = self.temp_file_prefix + "_temp_code.py"

        # Write code to temporary file
        async with aiofiles.open(filename, "w") as f:
            await f.write(code_to_execute)

        # Create namespace for execution
        namespace = {}
        
        try:
            async with aiofiles.open(filename) as f:
                code_content = await f.read()

            exec(code_content, namespace, namespace)
            evaluation = CodeEvaluation(
                passes_criteria=True,
                feedback=""
            )
        except Exception as e:
            evaluation = CodeEvaluation(
                passes_criteria=False, 
                feedback=f"Code execution failed: {e}"
            )
        finally:
            # Clean up temp file
            if os.path.exists(filename):
                print("stage when you remove the file")
                #os.remove(filename)
        
        if not evaluation.passes_criteria and evaluation.feedback:
            messages.append(("user", f"Please revise the code based on this feedback: {evaluation.feedback}"))
        
        return {
            "messages": messages,
            "evaluation": evaluation,
            "current_code": code_to_execute
        }

    def _should_continue(self, state: State):
        """Determine whether to continue iteration"""
        if state["evaluation"].passes_criteria:
            print("---CODE PASSED EVALUATION---")
            return "end"
        elif state["iterations"] >= self.max_iterations:  # Use max_iterations from instance
            print("---MAX ITERATIONS REACHED---")
            return "end"
        else:
            print("---CONTINUING TO NEXT ITERATION---")
            return "generate"

    def _setup_workflow(self):
        """Create and setup the workflow graph"""
        workflow = StateGraph(State)
        workflow.add_node("generate", self._generate_code)
        workflow.add_node("evaluate", self._evaluate_code)

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

    async def generate_code_with_feedback(self):
        """
        Generate code using the feedback loop graph.
        
        Args:
            code_spec: The coding task/question
        
        Returns:
            dict: Final state containing messages, evaluation results, and iterations
        """
        initial_state = {
            "messages": [
                ("system", CODE_GENERATOR_SYSTEM_PROMPT),
                ("user", CODE_GENERATOR_USER_PROMPT.format(code_spec=self.code_spec))
            ],
            "iterations": 0
        }
        
        return await self.app.ainvoke(initial_state)
