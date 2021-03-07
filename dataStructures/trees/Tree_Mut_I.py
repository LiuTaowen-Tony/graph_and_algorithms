import abc

class Tree_Mut(metaclass=abc.ABCMeta):

    @abs.abstractmethod
    def set_parent(self, child, parent, weight):
        pass

    @abs.abstractmethod
    def parent_of(self, child):
        pass

    @abs.abstractmethod
    def weight_of(self, child):
        pass

    @abs.abstractmethod
    def children_of(self, parent):
        """returns list of (child, weight) pair"""
        pass