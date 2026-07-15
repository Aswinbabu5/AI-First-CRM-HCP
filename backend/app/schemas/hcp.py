from pydantic import BaseModel, ConfigDict


class HcpResponse(BaseModel):
    id: int
    name: str
    specialization: str | None = None
    hospital_name: str | None = None
    email: str | None = None
    ph_no: str | None = None

    model_config = ConfigDict(from_attributes=True)