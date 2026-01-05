from fastapi import FastAPI

app = FastAPI(title="Responsable Relation Client IA")

@app.get("/")
def healthcheck():
    return {"status": "ok"}