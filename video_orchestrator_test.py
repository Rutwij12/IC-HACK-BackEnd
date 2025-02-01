from src.video_orchestrator import VideoOrchestrator
from dotenv import load_dotenv
import asyncio

async def main():
    # First load env variables
    load_dotenv(override=True)
    
    video_prompt = """
    Create a video explaining matrix multiplication
    """
    
    orchestrator = VideoOrchestrator(
        video_prompt,
        model="claude-3-5-sonnet-20241022"
    )
    result = await orchestrator.orchestrate_video()
    
    print("\nFinal Generated Result:")
    print("=" * 50)
    print(result)
    print("=" * 50)
    
    # Print the scene ideas
    print("\nGenerated Scene Ideas:")
    print("=" * 50)
    for scene in result["scene_ideas"]:
        print(f"\nScene \n{scene}:")
    
    # Print the scene plans
    print("\nGenerated Scene Plans:")
    print("=" * 50)
    for i, plan in enumerate(result["scene_plans"], 1):
        print(f"\nScene {i} Plan:")
        print(plan)
    
    # Print the final combined code
    print("\nFinal Combined Code:")
    print("=" * 50)
    print(result["final_code"])

if __name__ == "__main__":
    asyncio.run(main()) 