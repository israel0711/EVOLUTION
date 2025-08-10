from pydantic import BaseModel

class EvolutionDataCreate(BaseModel):
    name: str
    level: int
    experience: int
    description: str | None = None

class EvolutionDataUpdate(BaseModel):
    name: str | None = None
    level: int | None = None
    experience: int | None = None
    description: str | None = None
