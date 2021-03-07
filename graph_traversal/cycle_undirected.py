from data_structure.graphs.Graph_I import Graph

def cycle_undirected(graph : Graph, initial_node = 0):
    visited = [False] * graph.num_of_nodes()
    parent = [-1] * graph.num_of_nodes()

    def helper(current):
        visited[current] = True
        for (child, _) in graph.get_adjacent_nodes():
            if visited[child] and child != parent[current]:
                return (current,child)
            elif not visited[child]:
                parent[child] = current
                pair = helper(child)
                if pair:
                    return pair

    return helper(initial_node)
