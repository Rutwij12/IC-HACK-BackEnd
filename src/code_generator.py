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
        # Trim any trailing whitespace from the response content
        cleaned_content = response.content.rstrip()
        messages.append(("assistant", cleaned_content))
        print(f"state of messages after call: {self.temp_file_prefix}")
        print(messages)
        return {
            "messages": messages,
            "iterations": iterations + 1
        }

    async def _evaluate_code(self, state: State):
        """Evaluate generated code using manim --dry_run"""
        messages = state["messages"]
        
        # Concatenate all recent assistant messages until a non-assistant message
        last_message = ""
        for msg_type, content in reversed(messages):
            if msg_type == "assistant" and content and not isinstance(content, list):
                last_message = content + last_message
            elif msg_type != "assistant":
                break
        
        if not last_message:
            return {
                "messages": messages,
                "evaluation": CodeEvaluation(
                    passes_criteria=False,
                    feedback="No valid assistant message found"
                )
            }

        # Initialize code_blocks before try block
        code_blocks = []
        
        try:
            code_blocks = re.findall(r'```python\n(.*?)```', last_message, re.DOTALL)
            if not code_blocks:
                # Fallback to looking for any code blocks if python-specific ones aren't found
                code_blocks = re.findall(r'```(.*?)```', last_message, re.DOTALL)
        except Exception as e:
            print(f"Error extracting code blocks: {e}")
            print(f"Last message: {last_message}")

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
            
            # Extract the class name from the code
            class_match = re.search(r'class\s+(\w+)\s*\(', code_content)
            if not class_match:
                return {
                    "messages": messages,
                    "evaluation": CodeEvaluation(
                        passes_criteria=False,
                        feedback="No class definition found in the code"
                    )
                }
            
            class_name = class_match.group(1)
            
            # Run manim with --dry_run using extracted class name
            command = ["manim", "--dry_run", filename, class_name]
            print(f"Running command: {' '.join(command)}")
            
            process = await asyncio.create_subprocess_exec(
                *command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            
            if process.returncode == 0:
                evaluation = CodeEvaluation(
                    passes_criteria=True,
                    feedback=""
                )
            else:
                def extract_error(error_string: str):
                    error_lines = error_string.splitlines()
                    error_message = ""
                    for i, line in enumerate(error_lines):
                        if "Error" in line:
                            error_message = "\n".join(error_lines[i:])
                            print(f"\nDry run failed with error:\n{error_message}")
                            break
                    return error_message
                error_message = extract_error(stderr.decode())
                print(f"error messsage extracted from file {filename}: {error_message}")
                evaluation = CodeEvaluation(
                    passes_criteria=False,
                    feedback=f"Code Execution: {error_message}"
                )
        except Exception as e:
            evaluation = CodeEvaluation(
                passes_criteria=False, 
                feedback=f"Code execution failed: {str(e)}"
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
            print("---CONTINUING TO NEXT ITERATION OF CODE GEN---")
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
