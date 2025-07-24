from pydantic import BaseModel

class Batch(BaseModel):
  quantity: int
  average_wight: float
  biomass: float
  