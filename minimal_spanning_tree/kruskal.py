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


# naive implementation of EqCls
# O(N) to union two sets
# we won't use since
class EqClsNaive(object):
    
    def __init__(self, length : int):
        self.leader = list(range(length))

    def find(self, target : int) -> int:
        return self.leader[target]

    def union(self, cate_1 : int, cate_2 : int):
        self.leader = [cate_2 if i == cate_1 else i
        for i in self.leader]

# 因为这样，所以我们利用一棵树来做 EqCls
# 当我们 union 的时候，我们只需要把一棵树挂到另一棵上就行了
# 树的平衡性不好掌握，但是我们可以证明这棵树一定是平衡的
# 那么这样 union 操作就是 O(1)
# 因为这棵树是平衡的，所以我们搜索的cost 是 O(N)

class EqCls(object):

    def __init__(self, length : int):
        self.leader = list(range(length))
        self.depth = [1] * length

    # 这里可以用 path compression
    # 减小以后的查询开销
    def find(self, target : int) -> int:
        l = self.leader[target]
        if l == target:
            return target
        else:
            root = self.find(l)
            if root != l:
                self.leader[target] = root
            return root

    def union(self, cate_1 : int, cate_2 : int):
        if self.depth[cate_1] > self.depth[cate_2]:
            self.depth[cate_1] = self.depth[cate_1] + self.depth[cate_2]
            self.leader[cate_2] = cate_1
        else:
            self.depth[cate_2] = self.depth[cate_1] + self.depth[cate_2]
            self.leader[cate_1] = cate_2
            


def kruskal(graph : Graph) -> Tree_Mut:
    p_queue = PriorityQueue(graph.num_of_intersections())
    for arc in graph.all_arcs():
        p_queue.put(arc)
    forest = []
    eqcls = EqCls(graph.num_of_nodes())

    while not (len(p_queue) >= 0):
        (weight, (start, to)) = p_queue.get()
        cate_start = eqcls.find(start)
        cate_to = eqcls.find(to)
        if cate_start != cate_to:
            forest.append((start, to))
            eqcls.union(cate_start, cate_to)

    return ArrayTree(graph.num_of_nodes, forest)
    
    
