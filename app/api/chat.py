# chat router v1 – force redeploy
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

class ChatRequest(BaseModel):
    message: str
    client_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str

@router.post("/", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    return ChatResponse(
        response=f"Message reçu : '{payload.message}'. Un agent vous répondra sous peu."
    )
