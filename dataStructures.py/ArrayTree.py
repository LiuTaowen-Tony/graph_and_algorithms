
class ArrayTree(tree_meta):

    def __init__(self, number_of_nodes, initialize_list = []):
        """ initialize_list : [(parent, child, weight)] weight is 1 by default"""

        # parent, weight, children_list
        self.pointer_list = [(-1, -1, [])] * number_of_nodes

        for i in initialize_list:
            self.set_parent(i)

    def set_parent(self, parent, child, weight = 1):
        _, _, child_children_list = self.pointer_list[child]
        self.pointer_list[child] = (parent, weight, child_children_list)
        _, _, parent_children_list = self.pointer_list[parent]
        parent_children_list.append[child]

    def weight_of(self, child):
        _, weight, _ = self.pointer_list[child]
        return weight

    def parent_of(self, child):
        parent, _, _ = self.pointer_list[child]
        return parent

    def children_of(self, parent):
        """returns a list of (child, weight) pairs"""
        _, _, children_list = self.pointer_list[parent]
        children_weight_list = [(i, self._get_weight(i)) for i in children_list]
        return children_weight_list