from graph_traversal.shortest_path import shortest_path_unweighted
from data_structure.graphs.MatrixGraph import MatrixGraph
from queue import PriorityQueue


if __name__ == "__main__":
    mat = [
        [0, 0, 1, 0, 1],
        [0, 0, 3, 1, 0],
        [1, 3, 0, 0, 2],
        [0, 1, 0, 0, 0],
        [1, 0, 2, 0, 0]
        ]
    
    graph = MatrixGraph(mat)
    print(graph.all_arcs())
    print(graph.num_of_intersections())
    pQueue = PriorityQueue(graph.num_of_intersections())
    for i in graph.all_arcs():
        pQueue.put(i)

    while(not pQueue.empty()):
        print(pQueue.get())