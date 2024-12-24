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


    def randomize_pop(self, speed_multiplier):

        import datetime
        starttime = datetime.datetime.now()
        x=0
        for i in range(100000):
            x+=i
        endtime = datetime.datetime.now()
        diff = endtime - starttime
        print('Job took: ', diff.days, diff.seconds, diff.microseconds)




