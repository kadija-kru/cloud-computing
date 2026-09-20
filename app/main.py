from fastapi import FastAPI
from .models import EventIn
from .service import EventService

app = FastAPI(title="Event Ingestion & Risk Processing Service", version="1.0.0")
service = EventService()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return service.metrics()

@app.get("/events")
def list_events():
    return service.list_events()

@app.post("/events", status_code=201)
def ingest_event(event: EventIn):
    return service.ingest(event)
