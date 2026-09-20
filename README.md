# Event Ingestion & Risk Processing Service

A Python/FastAPI portfolio project that models a small event-driven service for ingesting operational events, deduplicating them, assigning risk, and exposing health/metrics endpoints.

## What this demonstrates

- FastAPI service design
- Typed request validation with Pydantic
- Deterministic event fingerprinting
- Duplicate-event suppression
- Risk classification rules
- Structured service boundaries
- Pytest coverage
- Docker packaging
- GitHub Actions CI

## Endpoints

- `POST /events` — ingest an event
- `GET /events` — list processed events
- `GET /health` — health check
- `GET /metrics` — lightweight processing counters

## Design decisions

Events receive a stable SHA-256 fingerprint from normalized source, event type, and message fields. Duplicate events return the existing record with `duplicate=true`.

Risk levels are deterministic:
- 8–10 → critical
- 6–7 → high
- 3–5 → medium
- 1–2 → low

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test

```bash
pytest
```

## Portfolio relevance

Cloud/backend engineering, event processing, observability, API design, deduplication, risk classification, testing, Docker, CI.
