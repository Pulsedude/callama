from dotenv import load_dotenv
import ollama
import os

load_dotenv(dotenv_path="./.env")
model_name = os.getenv("MODEL")


def ask(prompt_or_query: str) -> str:
    try:
        response = ollama.generate(
            model=model_name,
            prompt=prompt_or_query
        )
        return response["response"]
    except Exception as e:
        return tuple((False, str(e)))

