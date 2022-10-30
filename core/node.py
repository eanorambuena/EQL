from __future__ import annotations


class Node:

    _id = 0
    def __init__(self, value) -> None:
        Node._id += 1
        self.id = Node._id
        self.value = value
        self.pointers = {}

    def __repr__(self) -> str:
        children = ', '.join([repr(child) for child in list(self.pointers.values())]) or ";"
        if children == ";":
            return f"<{self.id}: {self.value}>"
        return f"<{self.id}: {self.value}: {children}>"

    def __str__(self) -> str:
        return self.connected_repr()

    def append(self, node: Node) -> bool:
        if node.id in self.pointers.keys():
            return False
        
        self.pointers[node.id] = node
        return True

    def connected_repr(self) -> str:
        return f"|{self.id}: {self.value}>"

    def next(self):
        if len(list(self.pointers.values())) > 0:
            return list(self.pointers.values())[0]
        
        return None
