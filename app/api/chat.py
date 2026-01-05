from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from app.services.agent import ChatAgent

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


# ---------- INIT AGENT ----------
agent = ChatAgent()


# ---------- GET (navigateur) ----------
@router.get("/")
def chat_info():
    return {
        "info": "Utilisez POST /chat avec un body JSON"
    }


# ---------- POST (API réelle) ----------
@router.post("/", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    reply = agent.reply(
        message=payload.message,
        client_id=payload.client_id
    )

    return ChatResponse(response=reply)
