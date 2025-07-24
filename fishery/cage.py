from pydantic import BaseModel
from fishery.site import Site
from fishery.batch import Batch
from datetime import date
import polars as pl

class Cage(BaseModel):
  name: str
  site: Site
  batches: list[Batch]
  active: bool
  start_date: date
  history: pl.DataFrame