from graphs import matrix_graph

def topological_sorting(graph):
    entered = []
    exited = []
    index = len(graph) - 1
    parent = []
    ts = []

    def dfsts(graph, initial_node):
        entered[initial_node] = True
        for (node, direction) in graph.get_adjacent_nodes(initial_node):
            if entered[node] and not exited[node]:
                print("there is a cycle!!")
                return
            else:
                parent[y] = x
                dfsts(y)
            exited[x] = True
            ts[index] = x
            index = index - 1

    for i in len(graph):
        if not entered[x]:
            dfsts(x)