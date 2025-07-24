from pydantic import BaseModel, Field
from fishery.site import Site
from fishery.batch import Batch
from datetime import date
from typing import Optional
import polars as pl

class Cage(BaseModel):
  name: str
  site: Optional[Site] = None
  batches: list[Batch] = Field(default_factory=list)
  active: bool = False
  start_date: Optional[date] = None
  history: pl.DataFrame