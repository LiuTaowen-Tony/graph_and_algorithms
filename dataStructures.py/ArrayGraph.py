
# class ArrayGraph(Graph):
#     def __init__(self, init_list):
#         """
#         [[(1,3), (2,4)],
#         [(0,3), (2,1)],
#         [(0,2), (1,2), (2,4)]]    
#             represents 
#             node0 --3--> node1 node0 --4--> node2
#             node1 --3--> node0 node1 --1--> node2
#             ...
#         """
#         self.poiter_list = init_list
#         self.data_list = []

#     def get_adjacent_nodes(self,node_number):
#         """returns list of (node_number, weight) pairs"""
#         return self.poiter_list[node_number]
