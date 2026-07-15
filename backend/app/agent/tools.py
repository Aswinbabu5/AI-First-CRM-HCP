from datetime import date

from langchain_core.tools import tool

from app.database import SessionLocal
from app.models.hcp import Hcp
from app.models.interaction import Interaction


@tool
def log_interaction(
    hcp_name: str,
    interaction_type: str,
    interaction_date: str,
    topics_discussed: str,
    interaction_time: str = "",
    attendees: str = "",
    materials_shared: str = "",
    samples_distributed: str = "",
    sentiment: str = "",
    outcomes: str = "",
    follow_up_actions: str = "",
    summary: str = "",
) -> dict:
    """
    Log a new interaction with an HCP in the CRM database.
    """

    db = SessionLocal()

    try:
        hcp = (
            db.query(Hcp)
            .filter(Hcp.name.ilike(hcp_name))
            .first()
        )

        if not hcp:
            return {
                "success": False,
                "error": f"HCP '{hcp_name}' was not found"
            }

        interaction = Interaction(
            hcp_id=hcp.id,
            interaction_type=interaction_type,
            interaction_date=date.fromisoformat(interaction_date),
            interaction_time=interaction_time,
            attendees=attendees,
            topics_discussed=topics_discussed,
            materials_shared=materials_shared,
            samples_distributed=samples_distributed,
            sentiment=sentiment,
            outcomes=outcomes,
            follow_up_actions=follow_up_actions,
            summary=summary,
        )

        db.add(interaction)
        db.commit()
        db.refresh(interaction)

        return {
            "success": True,
            "interaction_id": interaction.id,
            "hcp_id": hcp.id,
            "hcp_name": hcp.name,
            "interaction_type": interaction.interaction_type,
            "interaction_date": str(interaction.interaction_date),
            "interaction_time": interaction.interaction_time or "",
            "attendees": interaction.attendees or "",
            "topics_discussed": interaction.topics_discussed or "",
            "materials_shared": interaction.materials_shared or "",
            "samples_distributed": interaction.samples_distributed or "",
            "sentiment": interaction.sentiment or "",
            "outcomes": interaction.outcomes or "",
            "follow_up_actions": interaction.follow_up_actions or "",
            "summary": interaction.summary or ""
        }

    except ValueError:
        db.rollback()

        return {
            "success": False,
            "error": "Date must use YYYY-MM-DD format"
        }

    except Exception as exc:
        db.rollback()

        return {
            "success": False,
            "error": str(exc)
        }

    finally:
        db.close()

@tool
def edit_interaction(
    interaction_id: int,
    interaction_type: str | None = None,
    interaction_date: str | None = None,
    interaction_time: str | None = None,
    attendees: str | None = None,
    topics_discussed: str | None = None,
    materials_shared: str | None = None,
    samples_distributed: str | None = None,
    sentiment: str | None = None,
    outcomes: str | None = None,
    follow_up_actions: str | None = None,
    summary: str | None = None,
) -> dict:
    """
    Edit an existing HCP interaction.
    Only provided fields will be updated.
    """

    db = SessionLocal()

    try:
        interaction = (
            db.query(Interaction)
            .filter(Interaction.id == interaction_id)
            .first()
        )

        if not interaction:
            return {
                "success": False,
                "error": "Interaction not found"
            }

        updates = {
            "interaction_type": interaction_type,
            "interaction_time": interaction_time,
            "attendees": attendees,
            "topics_discussed": topics_discussed,
            "materials_shared": materials_shared,
            "samples_distributed": samples_distributed,
            "sentiment": sentiment,
            "outcomes": outcomes,
            "follow_up_actions": follow_up_actions,
            "summary": summary
        }

        changed_fields = {}

        if interaction_date is not None:
            interaction.interaction_date = date.fromisoformat(
                interaction_date
            )

            changed_fields["interaction_date"] = interaction_date

        for field, value in updates.items():
            if value is not None:
                setattr(interaction, field, value)
                changed_fields[field] = value

        if not changed_fields:
            return {
                "success": False,
                "error": "No update fields were provided"
            }

        db.commit()
        db.refresh(interaction)

        return {
            "success": True,
            "interaction_id": interaction.id,
            "hcp_id": interaction.hcp_id,
            "interaction_type": interaction.interaction_type or "",
            "interaction_date": str(interaction.interaction_date),
            "interaction_time": interaction.interaction_time or "",
            "attendees": interaction.attendees or "",
            "topics_discussed": interaction.topics_discussed or "",
            "materials_shared": interaction.materials_shared or "",
            "samples_distributed": interaction.samples_distributed or "",
            "sentiment": interaction.sentiment or "",
            "outcomes": interaction.outcomes or "",
            "follow_up_actions": interaction.follow_up_actions or "",
            "summary": interaction.summary or "",
            "changed_fields": changed_fields
        }

    except ValueError:
        db.rollback()

        return {
            "success": False,
            "error": "Date must use YYYY-MM-DD format"
        }

    except Exception as exc:
        db.rollback()

        return {
            "success": False,
            "error": str(exc)
        }

    finally:
        db.close()

@tool
def get_interaction(
    interaction_id: int
) -> dict:
    """
    Get a single HCP interaction by interaction ID.
    """

    db = SessionLocal()

    try:
        interaction = (
            db.query(Interaction)
            .filter(Interaction.id == interaction_id)
            .first()
        )

        if not interaction:
            return {
                "success": False,
                "error": "Interaction not found"
            }

        return {
            "success": True,
            "interaction_id": interaction.id,
            "hcp_id": interaction.hcp_id,
            "interaction_type": interaction.interaction_type or "",
            "interaction_date": str(interaction.interaction_date),
            "interaction_time": interaction.interaction_time or "",
            "attendees": interaction.attendees or "",
            "topics_discussed": interaction.topics_discussed or "",
            "materials_shared": interaction.materials_shared or "",
            "samples_distributed": interaction.samples_distributed or "",
            "sentiment": interaction.sentiment or "",
            "outcomes": interaction.outcomes or "",
            "follow_up_actions": interaction.follow_up_actions or "",
            "summary": interaction.summary or ""
        }

    except Exception as exc:
        return {
            "success": False,
            "error": str(exc)
        }

    finally:
        db.close()

@tool
def summarize_interaction(
    interaction_id: int
) -> dict:
    """
    Return the important details of an interaction
    so the AI agent can generate a concise summary.
    """

    db = SessionLocal()

    try:
        interaction = (
            db.query(Interaction)
            .filter(Interaction.id == interaction_id)
            .first()
        )

        if not interaction:
            return {
                "success": False,
                "error": "Interaction not found"
            }

        return {
            "success": True,
            "interaction_id": interaction.id,
            "interaction_type": interaction.interaction_type or "",
            "topics_discussed": interaction.topics_discussed or "",
            "materials_shared": interaction.materials_shared or "",
            "samples_distributed": interaction.samples_distributed or "",
            "sentiment": interaction.sentiment or "",
            "outcomes": interaction.outcomes or "",
            "follow_up_actions": interaction.follow_up_actions or "",
            "instruction": (
                "Create a short professional summary "
                "based on these interaction details."
            )
        }

    except Exception as exc:
        return {
            "success": False,
            "error": str(exc)
        }

    finally:
        db.close()

@tool
def suggest_follow_up(
    interaction_id: int
) -> dict:
    """
    Return interaction context so the AI agent can
    suggest an appropriate next follow-up action.
    """

    db = SessionLocal()

    try:
        interaction = (
            db.query(Interaction)
            .filter(Interaction.id == interaction_id)
            .first()
        )

        if not interaction:
            return {
                "success": False,
                "error": "Interaction not found"
            }

        return {
            "success": True,
            "interaction_id": interaction.id,
            "sentiment": interaction.sentiment or "",
            "outcomes": interaction.outcomes or "",
            "topics_discussed": interaction.topics_discussed or "",
            "current_follow_up_actions":
                interaction.follow_up_actions or "",
            "instruction": (
                "Suggest one practical next follow-up action "
                "for the field representative."
            )
        }

    except Exception as exc:
        return {
            "success": False,
            "error": str(exc)
        }

    finally:
        db.close()