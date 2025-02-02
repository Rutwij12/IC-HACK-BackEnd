import asyncio
import sys

async def test_manim_dry_run():
    """
    Test function that demonstrates using manim --dry_run to validate
    scene code without rendering
    """
    filename = "scene_1_temp_code.py"
    scene_name = "VectorAddition"  # or get this dynamically
    
    try:
        # Read the file contents for logging/debugging
        with open(filename, "r") as f:
            code_content = f.read()
        
        print(f"Contents of {filename}:")
        print("-" * 40)
        print(code_content)
        print("-" * 40)
        
        # Run manim with --dry_run
        print("\nExecuting dry run...")
        process = await asyncio.create_subprocess_exec(
            "manim", "--dry_run", filename, scene_name,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        
        def extract_error(error_string: str):
            error_lines = error_string.splitlines()
            error_message = ""
            for i, line in enumerate(error_lines):
                if "Error" in line:
                    error_message = "\n".join(error_lines[i:])
                    print(f"\nDry run failed with error:\n{error_message}")
                    break
            return error_message

        # Check return code and output
        if process.returncode == 0:
            print("\nDry run completed successfully!")
            return True
        else:
            stderr = stderr.decode()
            print("whole error")
            print(stderr)
            print("extracted error message: ")
            print(extract_error(stderr))
            return False
            
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return False
    except Exception as e:
        print(f"Error during dry run: {str(e)}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_manim_dry_run())
    sys.exit(0 if success else 1) 