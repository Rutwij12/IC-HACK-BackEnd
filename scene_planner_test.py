from src.scene_planner import ScenePlanner
from dotenv import load_dotenv
import asyncio

async def main():
    # First load env variables
    load_dotenv(override=True)
    
    scene_prompt = """
    ### Introduction to eigenvectors
    # show the main equations that eigenvectors have
    """
    
    scene_planner = ScenePlanner(
        scene_prompt,
        planner_model="claude-3-haiku-20240307",
        evaluator_model="claude-3-haiku-20240307"
    )
    result = await scene_planner.generate_scene_with_feedback()
    
    print("\nFinal Generated Result:")
    print("=" * 50)
    print(result)
    print("=" * 50)
    
    # Print the final scene plan
    final_plan = result["current_plan"]
    print("\nFinal Generated Scene Plan:")
    print("=" * 50)
    print(final_plan)
    
    # Print evaluation results
    print("\nEvaluation Results:")
    print("=" * 50)
    print(f"Passes Criteria: {result['evaluation'].passes_criteria}")
    if result['evaluation'].feedback:
        print(f"Feedback: {result['evaluation'].feedback}")
    
    print(f"\nTotal Iterations: {result['iterations']}")

if __name__ == "__main__":
    asyncio.run(main()) 