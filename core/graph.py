from __future__ import annotations
from types import NoneType

from core import iter
from core.error import IdError
from core.node import Node


class Graph:

    def __init__(self, root = None, default_family = "bfs") -> None:
        self.set_default_family(default_family)
        self.root = None
        
        if type(root) == Node:
            self.root = root

    def __contains__(self, value) -> bool:
        results = self.iter(
            (lambda node, index: node.value == value),
            (lambda node, index: node.value == value)
        )
        return (True in results)

    def __repr__(self) -> str:
        results = self.iter(lambda node, index: repr(node))
        return "\n".join(results)

    def __str__(self) -> str:
        representation = repr(self.root)
        result = ""
        row = ""
        depth = -1
        for char in representation:
            if char in ",\n":
                continue
            elif char == "<":
                result += depth * 4 * " " + row.strip() + "\n"
                row = ""
                depth += 1
            elif char == ">":
                result += depth * 4 * " " + row.strip() + "\n"
                row = ""
                depth -= 1
            else:
                row += char
        
        lines = []
        for line in result.split("\n"):
            if line.strip() != "":
                lines.append(line)

        return "\n".join(lines)

    def alienate(self, id: int) -> Graph:
        node = self.use_node(id)
        parents = self.get_parents(id)
        for parent_node in parents:
            parent_node.pointers.pop(id)

        graph = Graph(node)
        return graph

    def append(self, id: int | NoneType = None, value = None) -> bool:
        if self.root is None or id is None:
            self.root = Node(value)
            return True

        node = self.use_node(id)
        return node.append(Node(value))

    def borrow(self, id: int) -> dict:
        node = self.use_node(id)
        children = node.pointers
        node.pointers = {}
        return children
    
    def copy(self, id: int) -> Graph:
        node = self.use_node(id)
        node_copy = Node(node.value)
        for pointer in node.pointers:
            node_copy.append(self.copy(pointer).root)
        graph = Graph(node_copy)
        return graph

    def find(self, value) -> int | NoneType:
        results = self.iter(
            (lambda node, index: node),
            (lambda node, index: node.value == value)
        )
        if not(value in self):
            return None
        return results[-1]

    def get_parents(self, id: int) -> list:
        results = self.iter(
            lambda iter_node, index: [index, (id in list(iter_node.pointers.keys()))]
            )
        
        parents = []
        for index in range(len(results)):
            if results[index][1]:
                print(results[index + 1][0])
                parent_node = self.use_node(results[index + 1][0])
                parents.append(parent_node)

        return parents

    def id(self, value) -> int | NoneType:
        results = self.iter(
            (lambda node, index: node.id),
            (lambda node, index: node.value == value)
        )
        if not(value in self):
            return None
        return results[-1]

    def iter(self,
             function = (lambda node, index: node),
             stop_condition = (lambda node, index: False),
             family = None
            ) -> list:
        
        if self.void():
            return None

        if family is None:
            family = self.default_family

        return family(self, function, stop_condition)

    def paste(self, id: int, graph: Graph) -> bool:
        node = self.use_node(id)
        return node.append(graph.root)

    def set_default_family(self, family_name: str) -> None:
        self.default_family: str = iter.FAMILIES[family_name]

    def use_node(self, id) -> Node:
        results = self.iter(
            (lambda node, index: node),
            (lambda node, index: node.id == id)
        )
        if results[-1].id != id:
            raise IdError(id)

        return results[-1]

    def void(self) -> bool:
        return self.root == None


if __name__ == "__main__":
    my_graph = Graph()
    my_graph.append(value = 13)
    my_graph.append(1, 55)
    my_graph.append(1, 98)
    my_graph.append(2, 76)
    my_graph.append(3, 27)
    my_graph.append(3, 45)
    my_graph.append(5, 67)
    my_graph.append(5, 89)
    my_graph.append(7, 12)
    print("BFS:", repr(my_graph), end = "\n\n", sep = "\n")
    my_graph.set_default_family("dfs")
    print("DFS:", repr(my_graph), end = "\n\n", sep = "\n")
    print(my_graph.id(48), end = "\n\n")
    print(my_graph)
    print("Alienating node 2")
    subgraph = my_graph.alienate(2)
    print("My graph")
    print(my_graph)
    print("Subgraph")
    print(subgraph)
    print("Borrowing children from node 3")
    children = my_graph.borrow(3)
    print("My graph")
    print(my_graph)
    print("Children")
    print(children)
    print("Adding children to node 3")
    mother = my_graph.use_node(3)
    mother.pointers = children
    print("My graph")
    print(my_graph)
    print("Copying node 5")
    copy = my_graph.copy(5)
    print("My graph")
    print(my_graph)
    print("Copy")
    print(copy)
    print("Pasting copy to node 1")
    my_graph.paste(1, copy)
    print("My graph")
    print(my_graph)
    print("Pasting subgraph to node 1")
    my_graph.paste(1, subgraph)
    print("My graph")
    print(my_graph)
