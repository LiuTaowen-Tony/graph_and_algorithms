class UWTree():

    def __init__(self, number_of_nodes, initialize_list=[]):
        """
        initialize_list = 
        """

        # parent
        self.parent_list = [-1] * number_of_nodes

        for i in initialize_list:
            self.set_parent(i)

    def set_parent(self, parent, child):
        """O(1)"""
        self.pointer_list[child] = parent

    def parent_of(self, child):
        """O(1)"""
        return self.parent_list[child]

    def children_of(self, parent):
        """O(N)"""
        children_list = []
        for c, p in enumerate(self.pointer_list):
            if p == parent:
                children_list.append(c)
        return children_list
