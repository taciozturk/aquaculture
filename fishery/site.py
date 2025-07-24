from pydantic import BaseModel, Field
from fishery.cage import Cage

class Site(BaseModel):
  name: str
  cages: list[Cage] = Field(default_factory=list)
  