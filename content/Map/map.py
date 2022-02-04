import numpy as np
import random as rd

MAP_WIDTH = 4
MAP_HEIGHT = 4


class Mini_Map:
    _next_ID = 0

    def __init__(self):
        self.Map_ID = Mini_Map._next_ID
        Mini_Map._next_ID += 1
        self.MapArr = np.zeros((MAP_HEIGHT * MAP_WIDTH, MAP_HEIGHT * MAP_WIDTH))

    def map_gen(self):
        prob = 0.5
        pos = (0, 0)
        while pos[0] <= MAP_WIDTH and pos[1] <= MAP_HEIGHT:

            next_pos_prob = rd.random()

            if next_pos_prob >= prob:  # shift down
                pos[0] += 1
                self.MapArr[pos[0]]
            else:  # otherwise shift leftward
                pos[1] += 1
