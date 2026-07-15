from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class InteractionCreate(BaseModel):
    hcp_id: int
    interaction_type: str = Field(min_length=1, max_length=50)
    interaction_date: date
    interaction_time: str | None = None

    attendees: str | None = None
    topics_discussed: str | None = None
    materials_shared: str | None = None
    samples_distributed: str | None = None

    sentiment: str | None = None
    outcomes: str | None = None
    follow_up_actions: str | None = None
    summary: str | None = None


class InteractionUpdate(BaseModel):
    hcp_id: int | None = None
    interaction_type: str | None = None
    interaction_date: date | None = None
    interaction_time: str | None = None

    attendees: str | None = None
    topics_discussed: str | None = None
    materials_shared: str | None = None
    samples_distributed: str | None = None

    sentiment: str | None = None
    outcomes: str | None = None
    follow_up_actions: str | None = None
    summary: str | None = None


class InteractionResponse(InteractionCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)