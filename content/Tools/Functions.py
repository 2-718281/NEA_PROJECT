# random functions goes here

class Graph:
    def __init__(self, node_num):
        self.nodes_num = node_num
        self.adjmat = [[0 for i in range(self.nodes_num)] for i in range(self.nodes_num)]  # adjacency matrix
        self.node = []  # node content

    def add_node(self,node):
        self.node_con.append(node)

    def add_link(self, nodeA, nodeB):
        self.adjmat[nodeA,nodeB] = 1
        self.adjmat[nodeB,nodeA] = 1

    def del_link(self, nodeA, nodeB):
        self.adjmat[nodeA,nodeB] = 0
        self.adjmat[nodeB,nodeA] = 0

    def return_graph(self):
        return self.adjmat

