# random functions goes here

class Graph:

    def __init__(self, node_num):
        self.nodes = node_num
        self.adjmat = [[0 for i in range(self.nodes)] for i in range(self.nodes)]

    def add_link(self, nodeA, nodeB):
        self.adjmat[nodeA,nodeB] = 1
        self.adjmat[nodeB,nodeA] = 1

    def del_link(self, nodeA, nodeB):
        self.adjmat[nodeA,nodeB] = 0
        self.adjmat[nodeB,nodeA] = 0

