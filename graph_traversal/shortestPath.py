from dataStructures.graphs.Graph_I import Graph
from dataStructures.graphs.MatrixGraph import MatrixGraph
from collections import deque as Queue


def shortestPathUnweighted(graph: Graph, start: int, end: int):
    """
    input: unWeighted graph, start, end
    returns: distance from start to end
    """

    visited = [False] * graph.num_of_nodes()
    distanceFrom = [0] * graph.num_of_nodes()
    print(visited)
    queue = Queue()

    visited[end] = True
    distanceFrom[end] = 0

    queue.append(end)

    while (len(queue) > 0):
        current = queue.popleft()
        for child, weight in graph.adjacent_nodes_of(current):
            if not visited[child]:
                visited[child] = True
                # parent[child] = current
                distanceFrom[child] = distanceFrom[current] + 1
                queue.append(child)

    return distanceFrom[start]
