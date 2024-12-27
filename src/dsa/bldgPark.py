from . import lanePark
import pyray as rl

class ParkBldg:
    def __init__(self, numOfLanes, numOfSpaces, screen_width, screen_height):
        self.bldg = [lanePark.ParkLane(numOfSpaces) for _ in range(numOfLanes)]

        # takes up xx/xx of the screen width (left aligned)
        # divide by number of parkspaces minus the gaps
        self.indiv_space_width = int(((screen_width*2.2 // 4) // numOfSpaces) * 0.7)

        # takes up all screen heigh
        # only has xx/xx of screen height 
        # divide by number of lanes minus gaps
        self.indiv_space_height = int(((screen_height*1.7 // 3) // numOfLanes) * 0.7 )

        # 10% of the width
        # also limit it to 30 by choose whichever is the minimal
        self.gap_width = min(self.indiv_space_width // 10, 30)
        self.gap_height = min(self.indiv_space_height // 10, 30)


    def __repr__(self):
        return f'{self.bldg}'

    def __len__(self):
        return len(self.bldg)

    def __iter__(self):
        return iter(self.bldg)

    def __getitem__(self, index):
        return self.bldg[index]




