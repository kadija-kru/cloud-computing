from pydantic import BaseModel, Field

class EventIn(BaseModel):
    source: str = Field(min_length=1)
    event_type: str = Field(min_length=1)
    severity: int = Field(ge=1, le=10)
    message: str = Field(min_length=1)
