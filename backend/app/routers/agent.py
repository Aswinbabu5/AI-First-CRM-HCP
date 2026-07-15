import json

from fastapi import APIRouter, HTTPException

from app.agent.graph import Agent_Graph
from app.schemas.agent import AgentChatRequest

router = APIRouter(
    prefix="/agent",
    tags=["AI Agent"]
)

@router.post("/chat")
def chat_with_agent(payload: AgentChatRequest):
    try:
        result = Agent_Graph.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": payload.message
                    }
                ]
            }
        )

        messages = result.get("messages", [])

        if not messages:
            raise HTTPException(
                status_code=500,
                detail="Agent returned no response"
            )

        final_message = messages[-1]

        tool_used = None
        tool_data = None

        # Find the latest tool result
        for message in reversed(messages):
            if getattr(message, "type", None) == "tool":
                tool_used = getattr(message, "name", None)

                content = message.content

                if isinstance(content, dict):
                    tool_data = content

                elif isinstance(content, str):
                    try:
                        tool_data = json.loads(content)
                    except json.JSONDecodeError:
                        tool_data = None

                break

        return {
            "message": final_message.content,
            "tool_used": tool_used,
            "data": tool_data
        }

    except HTTPException:
        raise

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Agent processing failed: {str(exc)}"
        )