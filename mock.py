import numpy as np
import polars as pl
from datetime import datetime

def create_temperature(
  start_date: str, 
  end_date: str, 
  min_temp: int, 
  max_temp: int, 
  daily_variation: float):
  
  start: datetime = datetime.strptime(start_date, '%Y-%m-%d')
  end: datetime = datetime.strptime(end_date, '%Y-%m-%d')
  
  dates: pl.Series = pl.date_range(start, end, interval='1d', eager= True)
  day_of_year: pl.Series = dates.dt.ordinal_day()
  
  amplitude: float = (max_temp - min_temp) / 2
  mean: float = (max_temp + min_temp) / 2
  
  seasonal_temp: np.ndarray = mean + (amplitude * np.sin(2 * np.pi * (day_of_year - 81) / 365))
  
  np.random.seed(31)
  daily_noise: np.ndarray = np.random.uniform(-daily_variation, daily_variation, len(dates))
  
  temperature: np.ndarray = seasonal_temp + daily_noise
  
  return pl.DataFrame({
    'date': dates,
    'temperature': temperature 
  })

def create_sfr_table():
  pass

def create_mortality_rate_table():
  pass