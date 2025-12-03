import os
import argparse
from google.genai import types
from google import genai
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")
    
    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Generate content using Gemini API")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("prompt", type=str, help="User prompt")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.prompt)])]

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )
    
    if not response.usage_metadata:
        raise RuntimeError("No usage metadata found in the response")
    if args.verbose is True:
        print(f"User Prompt: {args.prompt}")
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))
    print("Response: " + "\n" + response.text)





if __name__ == "__main__":
    main()
    
