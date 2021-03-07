import abc

class Graph(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def adjacent_nodes_of(self,node_number):
        """returns a list of (node_number, weight) pairs"""
        pass

    @abc.abstractmethod
    def update_arc(self,start,end,weight):
        pass

    @abc.abstractmethod
    def num_of_nodes(self):
        pass

    @abc.abstractclassmethod
    def weight_between(self, start, end):
        pass