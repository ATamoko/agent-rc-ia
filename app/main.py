from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(title="Responsable Relation Client IA")

# Brancher les routes
app.include_router(chat_router)


@app.get("/")
def healthcheck():
    return {"status": "ok"}