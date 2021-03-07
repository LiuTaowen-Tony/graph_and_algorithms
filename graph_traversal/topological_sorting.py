from data_structure.graphs.Graph_I import Graph

# 有一个图表示一个 dependency 顺序
# 用 dfs 来遍历图，根据退出 node 的顺序来排序
# 这里没用栈表示退出，而是用了exited分开来表示
# 也可以用 bfs 遍历图，但是要转化成 arc (from, to) 的形式，用入度来算
# 时间复杂度是一样的

def topological_sorting(graph : Graph):
    """
    Args:
        graph : a directed graph with n nodes
    Returns:
        topological sort of graph as array ts of nodes if graph is
        acyclic (else bort)
    """
    n = graph.num_of_nodes()
    cycle_flag = False

    entered = [False] * n
    exited = [False] * n 
    index = n - 1
    parent = [-1] * n
    ts = [-1] * n

    def dfsts(current : int):
        nonlocal entered, exited, parent, ts
        nonlocal cycle_flag, index
        entered[current] = True
        for node, _ in graph.get_adjacent_nodes(current):
            if entered[node] and not exited[node]:
                print("there is a cycle!!")
                cycle_flag = True
                return
            else:
                parent[node] = current
                dfsts(node)
            exited[current] = True
            ts[index] = current
            index = index - 1

    for i in range(n):
        if not entered[i]:
            dfsts(i)

    if not cycle_flag:
        return ts

    