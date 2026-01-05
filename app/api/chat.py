from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

# ---------- MODELS ----------

class ChatRequest(BaseModel):
    message: str
    client_id: Optional[str] = None


class ChatResponse(BaseModel):
    response: str


# ---------- GET (pour navigateur) ----------

@router.get("/")
def chat_info():
    return {
        "info": "Utilisez POST /chat avec un body JSON"
    }


# ---------- POST (API réelle) ----------

@router.post("/", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    return ChatResponse(
        response=f"Message reçu : '{payload.message}'. Un agent vous répondra sous peu."
    )
