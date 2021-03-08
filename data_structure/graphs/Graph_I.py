import abc

class Graph(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def adjacent_nodes_of(self,node_number):
        """returns a list of (node_number, weight) pairs"""
        pass
    
    @abc.abstractmethod
    def num_of_nodes(self):
        pass

    @abc.abstractmethod
    def weight_between(self, start, end):
        pass

    @abc.abstractmethod
    def all_arcs(self):
        """
        Returns: \n
        Tuple [int, Tuple[int, int]] \n
        (weight, (from, to))
        """
        pass
    
    @abc.abstractmethod
    def num_of_intersections(self):
        pass