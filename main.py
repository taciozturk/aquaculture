from fishery import Batch, Site, Cage
from fishery.enums import FishSpecies, CageStatus, TransactionType

def main():
    cage_1: Cage = Cage(name="Besi-01")
    cage_2: Cage = Cage(name="Besi-02")
    cage_3: Cage = Cage(name="Besi-03")
    site_1: Site = Site(name="Cesme")
    site_1.assign_cage(cage_1)
    site_1.assign_cage(cage_2)
    site_1.assign_cage(cage_3)
    print(cage_1)


if __name__ == "__main__":
    main()
