NORTH = 0; EAST = 1; SOUTH = 2; WEST = 3

class Robot(object):
    ADVANCE_DCT = {NORTH: (0, 1), EAST: (1,0), 
                   SOUTH: (0, -1), WEST: (-1, 0)}

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.coordinates = (x, y)
        self.bearing = bearing

    def turn_right(self):
        self.turn(1)

    def turn_left(self):
        self.turn(-1)

    def turn(self, n):
        self.bearing = (self.bearing+n) % 4

    def advance(self):
        c = self.coordinates
        d = self.ADVANCE_DCT[self.bearing]

        self.coordinates = tuple(c[i]+d[i] for i in range(len(c)))

    def simulate(self, instructions):
        step_dct = {'L': self.turn_left,
                    'R': self.turn_right,
                    'A': self.advance}

        for step in instructions:
            step_dct[step]()