from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_database
from app.models.hcp import Hcp
from app.schemas.hcp import HcpResponse

router = APIRouter(
    prefix="/hcps",
    tags=["HCP"]
)


@router.get("", response_model=list[HcpResponse])
def get_hcp(
    search: str | None = None,
    db: Session = Depends(get_database)
):
    query = db.query(Hcp)

    if search:
        query = query.filter(Hcp.name.ilike(f"%{search}%"))

    return query.order_by(Hcp.name.asc()).all()