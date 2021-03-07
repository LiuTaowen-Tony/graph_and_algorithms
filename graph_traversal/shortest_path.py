from data_structure.graphs.Graph_I import Graph
from data_structure.graphs.MatrixGraph import MatrixGraph
from collections import deque as Queue


def shortest_path_unweighted(graph: Graph, start: int, end: int):
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

def testShortestPathUnweighted():
    mat = [
        [0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0]
        ]

    graph = MatrixGraph(mat)
    print(shortest_path_unweighted(graph, 0, 3)) # 3
    print(shortest_path_unweighted(graph, 2, 3)) # 2
