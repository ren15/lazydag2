from typing import List

class Node:
    def __init__(self, name, inputs:List = None,fn=None):
        self.name = name
        self.inputs = inputs
        self.fn = fn
        self.output = None

class Graph:
    def __init__(self):
        self.nodes = {}
    def add_node(self,name:str, inputs:List = None,fn=None):
        self.nodes[name] = Node(name, inputs,fn)
    def set_value(self, name:str, value):
        self.nodes[name].output = value
    def compute(self, name:str):
        if self.nodes[name].inputs is not None:
            for node_name in self.nodes[name].inputs:
                self.compute(node_name)
            if self.nodes[name].fn is not None:
                print('computing', name, 'with', self.nodes[name].inputs)
                self.nodes[name].output = self.nodes[name].fn(*[self.nodes[node_name].output for node_name in self.nodes[name].inputs])

def f1(high, low):
    print('computing f1')
    return high + low
def f2 (f1, low):
    print('computing f2')
    return f1 + low
def f3(f1, f2):
    print('computing f3')
    return f1 * f2
def f4(high, f1):
    print('computing f4')
    return high - f1


if __name__ == '__main__':

    """
    When we need f3 to update, we need to update f1 and f2, but not f4.
    """

    g = Graph()

    g.add_node('high')
    g.add_node('low')
    g.add_node('f1', inputs=['high', 'low'],fn=f1)
    g.add_node('f2', inputs=['f1', 'low'],fn=f2)
    g.add_node('f3', inputs=['f1', 'f2'],fn=f3)
    g.add_node('f4', inputs=['high', 'f1'],fn=f4)

    g.set_value('high', 2)
    g.set_value('low', 1)

    g.compute('f3')
    print(g.nodes['f3'].output)

    g.set_value('high', 3)
    g.compute('f3')
    print(g.nodes['f3'].output)



