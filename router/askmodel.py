from fastapi import APIRouter, status, HTTPException
from model import ask, model_name

router = APIRouter()


@router.get("/model/ask", status_code=status.HTTP_200_OK)
def ask_to_model(query: str):
    try:
        model_ask = ask(prompt_or_query=query)
        if isinstance(model_ask, tuple):
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(model_ask[1]))
        return {"query": query, "model": model_name, "response": model_ask}

    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
