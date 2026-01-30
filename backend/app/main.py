from fastapi import FastAPI
from app.models import Quiz  # Ensure models are imported for metadata creation
from app.db import Base, engine

app = FastAPI(
    title="Wiki Quiz Generator",
    version="1.0.0"
)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Wiki Quiz API running in Docker 🚀"
    }
