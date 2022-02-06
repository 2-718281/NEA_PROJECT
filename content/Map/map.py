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

    def Gene_proc(self):
        start_node = 0
        prob = 0.5
        terminate = False

        while not terminate:

            node_left = max(0,start_node-1)
            node_right = min(start_node+1, self.nodes)
            node_up =  max(0,start_node + MAP_WIDTH)
            node_down = min(start_node - MAP_WIDTH, self.nodes)
            nodelist = [node_right, node_left, node_down, node_up]

            new_node = start_node
            while new_node == start_node:
                new_node = rd.choice(nodelist)
            self.map.add_link(start_node,new_node)
            start_node = new_node





