# from data_structure.graphs.Graph_I import Graph

# def topological_sorting(graph : Graph):
#     entered = []
#     exited = []
#     index = len(graph) - 1
#     parent = []
#     ts = []

#     def dfsts(graph : Graph, current : int):
#         entered[current] = True
#         for (node, direction) in graph.get_adjacent_nodes(current):
#             if entered[node] and not exited[node]:
#                 print("there is a cycle!!")
#                 return
#             else:
#                 parent[node] = current
#                 dfsts(graph, node)
#             exited[current] = True
#             ts[index] = current
#             index = index - 1

#     for i in len(graph):
#         if not entered[i]:
#             dfsts()