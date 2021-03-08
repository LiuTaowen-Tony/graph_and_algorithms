from data_structure.graphs.Graph_I import Graph
from heapq import *

# 我们可以用 heap 实现一个 priority queue 
# 他的效率是 (M log N)
# 对于稀疏图，我们有更好的效率 (当 M < N log N 时, i.e. (N (log N) ^2))
# 但是对于稠密图，我们的效率更差

# 暂时不实现

def prim_heap(graph : Graph):
    pqueue = heapify([])