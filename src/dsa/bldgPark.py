from . import lanePark

class ParkBldg:
    def __init__(self, numOfSpaces, numOfLanes):
        self.bldg = [lanePark.ParkLane(numOfSpaces) for _ in range(numOfLanes)]


    def __repr__(self):
        return f'{self.bldg}'

    def __len__(self):
        return len(self.bldg)

    def __iter__(self):
        return iter(self.bldg)

    def __getitem__(self, index):
        return self.bldg[index]




