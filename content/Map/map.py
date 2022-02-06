import numpy as np
import random as rd
from content.Tools import Functions as F

MAP_WIDTH = 4
MAP_HEIGHT = 4


class big_map:

    _next_ID = 0

    def __init__(self):
        self.Map_ID = big_map._next_ID
        big_map._next_ID += 1
        self.nodes = MAP_HEIGHT * MAP_WIDTH
        self.map = F.Graph(self.nodes)

    def gene_proc(self):
        start_node = 0
        prob = 0.5
        terminate = False
        while not terminate:
            nodelist = [start_node+1,]
            next_prob = rd.random()
            if next_prob <= prob:
                




