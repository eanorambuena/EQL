from core.linked_list import LinkedList
from core.node import Node
from core.utils import numberize


class DataRow(LinkedList):

    def __init__(self, *args) -> None:
        super().__init__()
        for arg in args:
            arg = numberize(arg)
            if type(arg) == str:
                if "\"" in arg or "\'" in arg:
                    arg: str = arg.replace("'", "").replace('"', '')
                else:
                    continue
            self.append(arg)

    def __str__(self) -> str:
        result =  super().__str__()
        return result.replace(",", " |").replace("[", "").replace("]", "")

    @property
    def root(self) -> Node:
        return self.head

    def str_justed_by(self, value) -> str:
        results = self.iter(
            (lambda node, index: repr(node.value).ljust(value).replace("'", '"')),
            (lambda node, index: False)
        )
        result = str(results)
        return result.replace(",", " |").replace("[", "").replace("]", "")
