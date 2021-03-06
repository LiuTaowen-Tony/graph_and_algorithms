from itertools import product
from data_structure.graphs.Graph_Mut_I import Graph_Mut

class MatrixGraph(Graph_Mut):

    def __init__(self, weight_matrix=[[]]):
        """[[0,3,4], \n
            [3,0,1], \n
            [2,2,4]] \n
            represents 
            node0 --3--> node1 node0 --4--> node2
            node1 --3--> node0 node1 --1--> node2
            ...
        """
        self.weight_matrix = weight_matrix

    def adjacent_nodes_of(self, node_number):
        """returns list of (node_number, weight) pairs"""
        return [x for x in enumerate(self.weight_matrix[node_number])
                if x[1] != 0]

    def update_arc(self, start, end, weight):
        self.weight_matrix[start][end] = weight

    def num_of_nodes(self):
        return len(self.weight_matrix)

    def weight_between(self, start, end):
        return self.weight_matrix[start][end]
    
    def __str__(self):
        return str(self.weight_matrix)

    def all_arcs(self):
        nlst = list(range(self.num_of_nodes()))
        w = lambda i, j: self.weight_between(i, j)
        return [(w(i, j), (i, j)) for i,j in product(nlst, nlst) 
            if w(i, j) != 0]

    def num_of_intersections(self):
        return len(self.all_arcs())