from dataStructures.graphs.Graph_Mut_I import Graph_Mut

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

    def get_adjacent_nodes(self, node_number):
        """returns list of (node_number, weight) pairs"""
        return [x for x in enumerate(weight_matrix[node_number])
                if x[1] != 0]

    def update_arc(self, start, end, weight):
        self.weight_matrix[start][end] = weight

    def num_of_nodes(self):
        return len(self.weight_matrix)

    def weight_between(self, start, end):
        return self.weight_matrix[start][end]
