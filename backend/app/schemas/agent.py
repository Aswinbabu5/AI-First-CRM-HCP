from pydantic import BaseModel, Field


class AgentChatRequest(BaseModel):
    message: str = Field(min_length=2)


class AgentChatResponse(BaseModel):
    message: str
    tool_used: str | None = None
    data: dict | None = None