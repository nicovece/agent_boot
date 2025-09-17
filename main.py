import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description="AI Agent Boot CLI")
    parser.add_argument("prompt", help="The prompt to send to the AI")
    parser.add_argument("--verbose", action="store_true", 
                       help="Enable verbose output showing tokens and prompt")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Get the prompt and verbose flag from parsed arguments
    prompt = args.prompt
    verbose = args.verbose

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
        ]
    
    print("Hello from agent-boot!")
    
    # Make the API call with the provided prompt
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )

    if verbose:
        print(f"User prompt: {prompt}")
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    else:
        print(response.text)


if __name__ == "__main__":
    main()
