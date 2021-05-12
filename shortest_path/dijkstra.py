from data_structure.graphs.Graph_I import Graph

# 本质上，dijkstra 和 prim 就是加了权重的 bfs
# dijkstra 和 prim 的不同点是
# prim 考虑的是每一步都选最小的
# dijkstra 考虑的是下一步和之前的总和是最小的

def dijkstra(graph : Graph, start : int, end : int) -> int:
    """

    """
    def select_minimum(fringe : list[bool], distance : list[int]) -> int:
        n = len(fringe)
        lst = [(distance[node], node) for node in range(n) if fringe[node]]
        weight, node = min(lst)
        return node

    n = graph.num_of_nodes()
    tree = [False] * n
    fringe = [False] * n
    parent = [-1] * n
    distance = [100000] * n

    tree[start] = True
    for current, weight in graph.adjacent_nodes_of(start):
        fringe[current] = True
        parent[current] = True
        distance[current] = weight

    while not tree[end] and any(fringe):
        current = select_minimum(fringe, distance)
        fringe[current] = False
        tree[current] = True
        print(current)
        for child, weight in graph.adjacent_nodes_of(current):
            if not tree[child] and fringe[child]:
                if distance[current] + weight < distance[child]:
                    distance[child] = distance[current] + weight
                    parent[child] = current
            if not tree[child] and not fringe[child]:
                fringe[child] = True
                distance[child] = distance[current] + weight
                parent[child] = current

    return distance[end]