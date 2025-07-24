from pydantic import BaseModel
from fishery.cage import Cage

class Site(BaseModel):
  name: str
  cages: list[Cage]
  