from data_structure.graphs.Graph_I import Graph
from data_structure.trees.Tree_Mut_I import Tree_Mut, ArrayTree

# 一开始 naive 的想法是：
#
# 先选一个 tree 的 root 然后把周围标记为 fringe
# 如果 fringe 非空
#     那么选择从 tree 到 fringe 最短的路径 (*)
#     把这个节点移到 tree
#     这个节点周围是 fringe
# 
# 但是因为 (*) 这个操作是 (N + M) 的 (N 个树节点，M个可能路径)
# 所以我们缓存一下最有可能更新的

# 这个暂时跑不起来

snd = lambda t : t[1]

def prim_MST_sort(graph: matrix_graph):
    temp = [(False, False, -1, -1)] * graph.num_of_nodes()
    # in_tree, in_fringe, parent, weight

    def main():
        # initialize fringe
        root = 0
        for node_num, weight in graph.get_adjacent_nodes(root):
            label_fringe(node_num)
            set_weight_parent(node_num, root, weight)

        while non_empty_fringe():
            # select minimum element according to weight
            f = min(temp, key=snd)
            # move selected f from fringe to tree
            label_tree(node_num)

            for y in graph.get_adjacent_nodes(f):
                if not is_in_tree(y):
                    if is_in_fringe(y) and graph.weight(f, y) < current_weight(y):
                        set_weight_parent(y, graph.weight(f, y), f)
                    elif not is_in_fringe(y):
                        label_fringe(y)
                        set_weight_parent(y, graph.weight(f, y), f)

        # construct tree
        generated_tree = ArrayTree(graph.num_of_nodes())

    def is_in_tree(node_num):
        in_tree, _, _, _ = temp[node_num]
        return in_tree

    def is_in_fringe(node_num):
        _, in_fringe, _, _ = temp[node_num]
        return in_fringe

    def current_weight(node_num):
        _, _, _, weight = temp[node_num]
        return weight

    def non_empty_fringe():
        return any(map(snd, temp))

    def set_weight_parent(node_num, parent, weight):
        temp[node_num] = (False, True, parent, weight)

    def label_fringe(node_num):
        _, _, parent, weight = temp[node_num]
        temp[node_num] = (False, True, parent, weight)

    def label_tree(node_num):
        _, _, parent, weight = temp[node_num]
        temp[node_num] = (True, False, parent, weight)

    return main()
