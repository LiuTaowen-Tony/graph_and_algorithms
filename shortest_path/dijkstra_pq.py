from queue import PriorityQueue
from data_structure.graphs.Graph_I import Graph

# 和 prim 类似，我们也可以用 priority queue 实现 dijkstra
# 不同情景下有不同的性能

# 这个不 work 因为 python 的 PriorityQueue 不能 decreaseKey

def dijkstra_pq(graph : Graph, start : int, end : int) -> int:
    p_queue = PriorityQueue()
    n = graph.num_of_nodes()
    key = [1000000] * n
    parent = [-1] * n
    tree = [False] * n
    
    p_queue.put((0, start))

    while not tree[end] and not (len(p_queue) == 0):
        current = p_queue.get()
        tree[current] = True
        for child,weight in graph.adjacent_nodes_of(current):
            if not tree[child]: # so that is fr