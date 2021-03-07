# class UWUDGraph():

#     def __init__(self, number_of_nodes, init_list=[[]]):
#         """init_list : [[neighbour]]"""
#         self.data = init_list

#     def adjacent_nodes_of(self, node_num):
#         return self.data[node_num]

#     def num_of_nodes(self):
#         return len(self.data)

#     def new_arc_between(self, here, there):
#         self.data[here].append(there)
#         self.data[there].append(here)

#     def del_arc_betweeen(self, here, there):
#         self.data[here].remove(there)
#         self.data[there].remove(here)
