from . import lanePark
import pyray as rl

class ParkBldg:
    def __init__(self, numOfLanes, numOfSpaces, screen_width, screen_height):
        self.bldg = [lanePark.ParkLane(numOfSpaces) for _ in range(numOfLanes)]

        # takes up 3/4 of the screen width (left aligned)
        # divide by number of parkspaces minus the gaps
        self.indiv_space_width = (screen_width*3 // 4) // numOfSpaces

        # takes up all screen heigh
        # only has 1/3 of screen height 
        # divide by number of lanes minus gaps
        self.indiv_space_height = (screen_height // 3) // numOfLanes

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




