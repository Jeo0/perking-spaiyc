from . import spacePark


class ParkLane:
    def __init__(self, howmany):
        self.lane = [spacePark.ParkSpace() for _ in range(howmany)]
        

    def __repr__(self):
        return f'{self.lane}'

    def __len__(self):
        return len(self.lane)

    def __iter__(self):
        return iter(self.lane)

    def __getitem__(self, index):
        return self.lane[index]




