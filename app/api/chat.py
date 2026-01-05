from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from app.services.agent import AgentService


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

agent = AgentService()

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
    response = agent.handle_message(
        message=payload.message,
        client_id=payload.client_id
    )

    return ChatResponse(response=response)
