from data_structure.graphs.Graph_I import Graph
from data_structure.trees.Tree_Mut_I import Tree_Mut
from data_structure.trees.ArrayTree import ArrayTree
from queue import PriorityQueue

# 每次都选择一个最短的路径，组成一个森林
# 用 priority queue
# 要求是组成的森林里没有环
# 用动态 equivalence classes

# 证明：
# 利用归纳法，假设过程中的某一步不是最小生成树的一部分
# i.e. arc(x, y) 不是最小生成树的一部分
# 那么至少存在一个不属于森林中的 arc(x', y') 使得 x, y 是联通的
# 但是根据算法 weight arc(x, y) < weight arc(x', y')
# 因此矛盾

def kruskal(graph : Graph) -> Tree_Mut:
    pQueue = PriorityQueue(graph.num_of_intersections())
    for arc in graph.all_arcs():
        pQueue.put(arc)
    
    
    
