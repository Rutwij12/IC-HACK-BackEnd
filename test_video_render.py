from src.video_orchestrator import VideoOrchestrator
from dotenv import load_dotenv
import asyncio

async def main():
    # First load env variables
    load_dotenv(override=True)
    
    video_prompt = """
    Create a short video showing a circle morphing into a square.
    Make it simple and quick - just 3-4 seconds long.
    """
    
    print("\nInitializing VideoOrchestrator...")
    orchestrator = VideoOrchestrator(
        video_prompt,
        model="claude-3-5-sonnet-20241022"
    )
    
    print("\nGenerating and rendering video...")
    print("=" * 50)
    result = await orchestrator.generate_and_render_video()
    
    print("\nGeneration and Rendering Complete!")
    print("=" * 50)
    
    print("\nOutput File Paths:")
    print("-" * 30)
    print(f"Video Path: {result['video_path']}")
    print(f"Thumbnail Path: {result['thumbnail_path']}")
    
    print("\nChecking if files exist...")
    print("-" * 30)
    import os
    if result['video_path'] and os.path.exists(result['video_path']):
        print(f"✅ Video file exists!")
        print(f"Size: {os.path.getsize(result['video_path']) / (1024*1024):.2f} MB")
    else:
        print("❌ Video file not found!")
        
    if result['thumbnail_path'] and os.path.exists(result['thumbnail_path']):
        print(f"✅ Thumbnail file exists!")
        print(f"Size: {os.path.getsize(result['thumbnail_path']) / 1024:.2f} KB")
    else:
        print("❌ Thumbnail file not found!")

if __name__ == "__main__":
    asyncio.run(main()) 