from sqlalchemy import Column, Integer, String

from app.database import Base

class Hcp(Base):
    __tablename__='Hcp'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    specialization = Column(String(150), nullable=True)
    hospital_name = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    ph_no = Column(String(15), nullable=True)