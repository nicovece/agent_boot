import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.run_python_file import schema_run_python_file, run_python_file
from functions.write_file import schema_write_file, write_file
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="AI Agent Boot CLI")
    parser.add_argument("prompt", help="The prompt to send to the AI")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output showing tokens and prompt")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get the prompt and verbose flag from parsed arguments
    prompt = args.prompt
    verbose = args.verbose

    # Initialize conversation with user's prompt
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    
    # Agent loop - maximum 20 iterations
    max_iterations = 20
    iteration = 0
    
    try:
        while iteration < max_iterations:
            iteration += 1
            
            if verbose:
                print(f"--- Iteration {iteration} ---")
            
            # Make the API call with the entire conversation history
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    tools=[available_functions],  # Pass the tools to the AI
                ),
            )
            
            # Add the model's response to the conversation
            for candidate in response.candidates:
                messages.append(candidate.content)
            
            # Check if the response contains function calls and collect all of them
            function_calls = []
            has_function_calls = False
            if hasattr(response.candidates[0].content, 'parts'):
                for part in response.candidates[0].content.parts:
                    if hasattr(part, 'function_call') and part.function_call is not None:
                        has_function_calls = True
                        function_calls.append(part.function_call)
            
            # Execute all function calls and collect results
            if function_calls:
                function_response_parts = []
                for function_call_part in function_calls:
                    # Use call_function to execute the function
                    function_call_result = call_function(function_call_part, verbose)
                    
                    # Extract the function response part
                    if (hasattr(function_call_result, 'parts') and 
                        len(function_call_result.parts) > 0 and
                        hasattr(function_call_result.parts[0], 'function_response')):
                        function_response_parts.append(function_call_result.parts[0])
                        
                        # Print the result if verbose is enabled
                        if verbose:
                            print(f"-> {function_call_result.parts[0].function_response.response}")
                    else:
                        raise Exception("call_function did not return expected types.Content structure")
                
                # Add all function results as a single user message
                if function_response_parts:
                    messages.append(types.Content(role="user", parts=function_response_parts))
            
            # If no function calls and we have text, we're done
            if not has_function_calls and response.text:
                print("Final response:")
                print(response.text)
                if verbose:
                    print(f"Total iterations: {iteration}")
                    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
                break
            
            # If no function calls and no text, something went wrong
            if not has_function_calls and not response.text:
                print("Error: Model returned no function calls and no text response")
                break
        
        # If we've reached max iterations
        if iteration >= max_iterations:
            print(f"Reached maximum iterations ({max_iterations}). Stopping.")
            
    except Exception as e:
        print(f"Error in agent loop: {e}")
        if verbose:
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
