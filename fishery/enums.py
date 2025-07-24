from enum import StrEnum

class FishSpecies(StrEnum):
  SEA_BASS = "sea_bass"
  SEA_BREAM = "sea_bream"

class CageStatus(StrEnum):
  ACTIVE = "active"
  HARVESTED = "harvested"
  PLANNING = "planning"
  TERMINATED = "terminated"
  
class TransactionType(StrEnum):
  ADJUSTMENT = "adjustment"
  HARVEST = "harvest"
  INPUT = "input"
  MORTALITY = "mortality"
  TRANSFER_IN = "transfer_in"
  TRANSFER_OUT = "transfer_out"
  