from hashlib import sha256
from .models import EventIn

class EventService:
    def __init__(self):
        self._events = {}
        self._processed = 0
        self._duplicates = 0

    def _fingerprint(self, event: EventIn) -> str:
        normalized = "|".join([
            event.source.strip().lower(),
            event.event_type.strip().lower(),
            event.message.strip().lower()
        ])
        return sha256(normalized.encode("utf-8")).hexdigest()

    def _risk(self, severity: int) -> str:
        if severity >= 8:
            return "critical"
        if severity >= 6:
            return "high"
        if severity >= 3:
            return "medium"
        return "low"

    def ingest(self, event: EventIn):
        fingerprint = self._fingerprint(event)
        if fingerprint in self._events:
            self._duplicates += 1
            existing = dict(self._events[fingerprint])
            existing["duplicate"] = True
            return existing

        self._processed += 1
        record = {
            "fingerprint": fingerprint,
            "source": event.source,
            "event_type": event.event_type,
            "severity": event.severity,
            "risk": self._risk(event.severity),
            "message": event.message,
            "duplicate": False
        }
        self._events[fingerprint] = record
        return record

    def list_events(self):
        return list(self._events.values())

    def metrics(self):
        return {
            "unique_events": len(self._events),
            "processed": self._processed,
            "duplicates": self._duplicates
        }
