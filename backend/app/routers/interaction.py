from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_database
from app.models.hcp import Hcp
from app.models.interaction import Interaction
from app.schemas.interaction import (
    InteractionCreate,
    InteractionResponse,
    InteractionUpdate,
)

router = APIRouter(
    prefix="/interactions",
    tags=["Interaction"]
)


@router.post(
    "",
    response_model=InteractionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_interaction(
    payload: InteractionCreate,
    db: Session = Depends(get_database)
):
    hcp = db.query(Hcp).filter(Hcp.id == payload.hcp_id).first()

    if not hcp:
        raise HTTPException(
            status_code=404,
            detail="HCP not found"
        )

    interaction = Interaction(**payload.model_dump())

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction


@router.get(
    "",
    response_model=list[InteractionResponse]
)
def get_interactions(
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_database)
):
    return (
        db.query(Interaction)
        .order_by(Interaction.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


@router.put(
    "/{interaction_id}",
    response_model=InteractionResponse
)
def update_interaction(
    interaction_id: int,
    payload: InteractionUpdate,
    db: Session = Depends(get_database)
):
    interaction = (
        db.query(Interaction)
        .filter(Interaction.id == interaction_id)
        .first()
    )

    if not interaction:
        raise HTTPException(
            status_code=404,
            detail="Interaction not found"
        )

    update_data = payload.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(interaction, field, value)

    db.commit()
    db.refresh(interaction)

    return interaction