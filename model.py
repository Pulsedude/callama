from dotenv import load_dotenv
from ollama import Client
import os

load_dotenv(dotenv_path="./.env")
model_name = os.getenv("MODEL")
host = os.getenv("OLLAMA_HOST")
client = Client(host=host)

def ask(prompt_or_query: str) -> str:
    try:
        response = client.generate(
            model=model_name,
            prompt=prompt_or_query
        )
        return response["response"]
    except Exception as e:
        return tuple((False, str(e)))

