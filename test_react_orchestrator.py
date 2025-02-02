import asyncio
from src.react_orchestrator import ReactOrchestrator

async def test_react_orchestrator():
    # Example prompt for creating a set of components that demonstrate sorting algorithms
    prompt = """Visualise matric multiplication and transformation"""
    
    try:
        # Initialize orchestrator
        orchestrator = ReactOrchestrator(prompt)
        
        # Run the orchestration
        print("Starting React component generation...")
        result = await orchestrator.orchestrate_components()
        
        # Print results from each stage
        print("\nComponent Ideas:")
        for i, idea in enumerate(result["component_ideas"], 1):
            print(f"\nComponent {i}:")
            print(idea)
        
        print("\nComponent Plans:")
        for i, plan in enumerate(result["component_codes"], 1):
            print(f"\nPlan {i}:")
            print(plan)
        
        print("\nFiles generated:")
        print("- src/components/Component*.tsx")
        print("- src/App.tsx")
        
        print("\nComponent generation completed successfully!")
        
    except Exception as e:
        print(f"Error during component generation: {str(e)}")
        raise e

if __name__ == "__main__":
    asyncio.run(test_react_orchestrator()) 