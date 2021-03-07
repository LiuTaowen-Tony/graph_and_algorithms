import abc
from dataStructures.graphs.Graph_I import Graph


class Graph_Mut(metaclass=Graph):

    @abc.abstractmethod
    def update_arc(self, start, end, weight):
        pass
