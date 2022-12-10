from typing import List
import inspect


class Node:
    def __init__(self, name, inputs: List, fn, graph):
        self.name = name
        self.inputs = inputs
        self.fn = fn
        self.output = None
        self.graph = graph
        self.inputs_mem = {}

    def get_inputs(self):
        return {
            node_name: self.graph.nodes[node_name].output for node_name in self.inputs
        }

    def invoke_fn(self):
        return self.fn(
            *[self.graph.nodes[node_name].output for node_name in self.inputs]
        )

    def compute(self):
        if self.inputs is not None:
            for node_name in self.inputs:
                self.graph.compute(node_name)
        if self.fn is not None and self.inputs is not None:
            # we can skip the computation if the inputs are the same
            if self.inputs_mem != self.get_inputs():
                print("computing", self.name, "with", self.inputs)
                self.output = self.invoke_fn()
                self.inputs_mem = self.get_inputs()


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name: str, inputs: List = None, fn=None):
        self.nodes[name] = Node(name, inputs, fn, self)

    def add_node_fn(self, fn=None):
        inputs = inspect.getfullargspec(fn).args
        self.nodes[fn.__name__] = Node(fn.__name__, inputs, fn, self)

    def set_value(self, name: str, value):
        self.nodes[name].output = value

    def compute(self, name: str):
        self.nodes[name].compute()

    def exec(self, name: str):
        self.compute(name)
        return self.nodes[name].output
