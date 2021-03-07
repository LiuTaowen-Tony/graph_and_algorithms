from graph_traversal.shortestPath import shortestPathUnweighted
from dataStructures.graphs.MatrixGraph import MatrixGraph


if __name__ == "__main__":
    mat = [
        [0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0]
        ]

    graph = MatrixGraph(mat)
    print(shortestPathUnweighted(graph, 2, 3))
    print(shortestPathUnweighted(graph, 1, 3))