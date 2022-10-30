from types import NoneType

from core.node import Node


class LinkedList:

    def __init__(self, head = None) -> None:
        self.head = None
        self.tail = None

        if type(head) in (list, tuple, LinkedList):
            for item in head:
                self.append(item)
        elif type(head) == Node:
            self.head = head
            self.tail = self.head

    def __contains__(self, value):
        results = self.iter(
            (lambda node, index: node.value == value),
            (lambda node, index: node.value == value)
        )
        return (True in results)

    def __getitem__(self, index):
        results = self.iter(
            (lambda node, index: node.value),
            (lambda node, node_index: node_index == index)
        )
        return results[index]

    def __setitem__(self, index, value):
        results = self.iter(
            (lambda node, node_index: node),
            (lambda node, node_index: node_index == index)
        )
        results[index].value = value

    def __len__(self) -> int:
        indexes = self.iter((lambda node, index: index))
        return len(indexes)

    def __repr__(self) -> str:
        results = self.iter(
            (lambda node, index: node.connected_repr()),
            (lambda node, node_index: False)
        )
        content = ", ".join(results)
        return f"[{content}]"

    def __str__(self) -> str:
        results = self.iter(
            (lambda node, index: node.value),
            (lambda node, node_index: False)
        )
        return str(results)

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.append(node)
            self.tail = node

    def index(self, value):
        results = self.iter(
            (lambda node, index: index),
            (lambda node, index: node.value == value)
        )
        if not(value in self):
            return None
        return len(results) - 1

    def insert(self, index, value) -> bool:
        results = self.iter(
            (lambda node, index: node),
            (lambda node, node_index: node_index == index)
        )
        before_node = results[-1]
        if before_node == None:
            return False

        after_node = before_node.next()
        before_node.pointers = {}
        node = Node(value)
        before_node.append(node)
        node.append(after_node)
        return True

    def iter(self, function, stop_condition = (lambda node, index: False)):
        node = self.head
        index = 0
        results = []
        end = False
        while (node is not None) and (not end):
            results.append(function(node, index))
            end = stop_condition(node, index)
            node = node.next()
            index += 1
        return results

    def pop(self, index = -1) -> NoneType | Node:
        last  = False
        if index == -1:
            index == len(self) - 1
            last = True
        results = self.iter(
            (lambda node, index: node),
            (lambda node, node_index: node_index == index)
        )
        before_node = results[-2]

        if before_node == None:
            return None

        node = before_node.next()
        before_node.pointers = {}

        if last:
            self.tail = before_node
            return node.value

        after_node = node.next()
        before_node.append(after_node)

        return node.value
        
if __name__ == "__main__":
    my_list = LinkedList(list(range(5, 19)))

    print(len(my_list), my_list.index(7), my_list[3])
    print(repr(my_list))

    print(my_list)
    my_list.insert(3, 88)
    print(my_list)
    for i in range(5):
        print(my_list.pop())
    print(my_list)
    my_list[6] = 27
    print(my_list)
