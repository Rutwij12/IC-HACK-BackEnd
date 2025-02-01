from src.code_generator import CodeGenerator
from dotenv import load_dotenv
import asyncio

async def main():
    # First load env variables
    load_dotenv(override=True)
    
    code_generator = CodeGenerator(
        ("write a python function demonstrating breadth first search, however initially you should make some syntax error, only output code with an error, no corrections required"
         ", before outputting any code, you must explain what syntax error you are about to make. Ignore all instructtions about geneating manim code, this is completeely unrealted to manim. Just a normal function required"), 
        temp_file_prefix="0",
        model="claude-3-haiku-20240307"
    )
    result = await code_generator.generate_code_with_feedback()
    
    print("\nFinal Generated Result:")
    print("=" * 50)
    print(result)
    print("=" * 50)
    
    # Print the final code
    final_code = result["messages"][-2][1]  # Get last assistant message before any feedback
    print("\nFinal Generated Code:")
    print("=" * 50)
    print(final_code)
    
    # Print evaluation results
    print("\nEvaluation Results:")
    print("=" * 50)
    print(f"Passes Criteria: {result['evaluation'].passes_criteria}")
    if result['evaluation'].feedback:
        print(f"Feedback: {result['evaluation'].feedback}")
    
    print(f"\nTotal Iterations: {result['iterations']}")

if __name__ == "__main__":
    asyncio.run(main()) 