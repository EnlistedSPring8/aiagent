import os
from google import genai
from dotenv import load_dotenv

def main():
    if api_key == None:
        raise RuntimeError("GEMINI_API_KEY is not set")
    print("Hello from ai-agent!")
    client.models.generate_content(
        model="gemini-1.5-flash",
        conents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

if __name__ == "__main__":
    main()
    
