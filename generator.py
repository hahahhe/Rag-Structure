# prompt

import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
client =  genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def build_prompt(query: str, documents: list[str]) -> str:
    context = "\n\n".join(documents)
    prompt = f"""
    아래 Context를 참고하여 Question에 답하시오.
    Context:
    {context}

    Question:
    {query}

    Answer:
    """

    return prompt

def generate(prompt: str, model = "gemini-3.6-flash") -> str:
    response = client.models.generate_content(model=model, contents=prompt)
    
    return response.text