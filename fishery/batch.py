from pydantic import BaseModel
from typing import Optional
from datetime import date

class Batch(BaseModel):
  start_date: Optional[date] = None
  quantity: Optional[int] = None
  average_wight: Optional[float] = None
  biomass: Optional[float] = None
  