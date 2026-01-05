from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(title="Responsable Relation Client IA")

# route santé
@app.get("/")
def healthcheck():
    return {"status": "ok"}

# branchement du router chat
app.include_router(chat_router)
