from _containers import UWUDGraph

def cycleUndirected(graph : Graph, initial_node = 0):
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

UWUDGraph()

triangle = ([[0,1,1],[0,0,1],[0,0,0]])