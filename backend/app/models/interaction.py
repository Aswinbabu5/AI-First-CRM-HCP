from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from app.database import Base

class Interaction(Base):
    __tablename__ = 'interaction'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    hcp_id = Column(
        Integer,
        ForeignKey("Hcp.id"),
        nullable=False
    )

    interaction_type = Column(String(50), nullable=False)
    interaction_date = Column(Date, nullable=False)
    interaction_time = Column(String(20), nullable=True)

    attendees = Column(Text, nullable=True)
    topics_discussed = Column(Text, nullable=True)
    materials_shared = Column(Text, nullable=True)
    samples_distributed = Column(Text, nullable=True)

    sentiment = Column(String(30), nullable=True)
    outcomes = Column(Text, nullable=True)
    follow_up_actions = Column(Text, nullable=True)
    summary = Column(Text, nullable=True)

    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )