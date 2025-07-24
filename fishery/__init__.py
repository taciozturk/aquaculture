from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional, Dict, Any
import polars as pl

class Batch(BaseModel):
  start_date: Optional[date] = None
  quantity: Optional[int] = None
  average_wight: Optional[float] = None
  biomass: Optional[float] = None

class Cage(BaseModel):
  name: str
  site_name: Optional[str] = None
  batches: list[Batch] = Field(default_factory=list)
  active: bool = False
  start_date: Optional[date] = None
  history_data: Dict[str, Any] = Field(default_factory=dict)
  
  @property
  def history(self) -> pl.DataFrame:
    if self.history_data:
      return pl.DataFrame(self.history_data)
    return pl.DataFrame()
  
  def set_history(self, df: pl.DataFrame):
    self.history_data = df.to_dict(as_series=False)
  
class Site(BaseModel):
  name: str
  cages: list[Cage] = Field(default_factory=list)
  
  def assign_cage(self, cage: Cage):
    cage.site_name = self.name
    self.cages.append(cage)
  

