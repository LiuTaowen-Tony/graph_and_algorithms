class MatrixGraph(graph_meta):

    def __init__(self,weight_matrix = [[]]):
        """[[0,3,4],
            [3,0,1],
            [2,2,4]]
            represents 
            node0 --3--> node1 node0 --4--> node2
            node1 --3--> node0 node1 --1--> node2
            ...
        """
        self.weight_matrix = weight_matrix

    def get_adjacent_nodes(self,node_number):
        """returns list of (node_number, weight) pairs"""
        return filter(
            (lambda t : t[0] != 0),
            enumerate(weight_matrix[node_number])
            )

    def update_arc(self,start, end,weight):
        self.weight_matrix[start][end] = weight

    def num_of_nodes(self):
        return len(self.weight_matrix)

    def weight_between(self,start,end):
        return self.weight_matrix[start][end]