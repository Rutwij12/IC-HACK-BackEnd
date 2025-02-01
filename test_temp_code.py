def test_code_execution():
    """
    Test function that demonstrates executing code from a temporary file
    similar to CodeGenerator._evaluate_code
    """
    # Create a namespace dictionary with globals for imports
    namespace = {}
    
    try:
        with open("scene_1_temp_code.py", "r") as f:
            code_content = f.read()
        
        print("Contents of temp_code.py:")
        print("-" * 40)
        print(code_content)
        print("-" * 40)
        
        # Execute the code with the namespace
        print("\nExecuting code...")
        exec(code_content, namespace, namespace)
        print("\nCode executed successfully!")
        
    except FileNotFoundError:
        print("Error: temp_code.py not found")
    except Exception as e:
        print(f"Error executing code: {str(e)}")

if __name__ == "__main__":
    test_code_execution() 