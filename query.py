import sys

from core import error
from core.graph import Graph
from core.linked_list import LinkedList
from core.node import Node
from core.utils import numberize


class DataBase(Graph):

    def __init__(self) -> None:
        super().__init__()
        self.root = Node(Row())
        self.preparing_insert = False
        self.where_clause = False
        self.last_selection = []
        self.env_variables = {
            "MAX_RESULTS_SHOWN": 10,
            "MIN_VALUE_LENGTH_SHOWN": 20,
        }
        self.defined_clauses = [
            "SELECT",
            "WHERE",
            "AND",
            "TEMPLATE",
            "LIST",
            "EXIT",
            "INSERT",
            "VALUES",
            "ENV",
            "CLAUSES",
            "SET"
        ]
        self.defined_clauses.sort()

    def insert(self, *args) -> None:
        self.append(1, Row(*args))

    def list(self, clause: str) -> None:
        if clause == 'env':
            print(*list(self.env_variables.keys()), sep = "\n")
        elif clause == 'clauses':
            print(*self.defined_clauses, sep = "\n")

    def query(self, query: str) -> None:
        query = query.lower()
        printing = query.endswith(';')
        if printing:
            query = query[:-1]
        query = query.split()
        if len(query) == 0:
            return
        instruction = query[0]

        try:
            if instruction == 'exit':
                sys.exit()

            elif instruction == 'select':
                result = self.select(query[1])
                self.query(' '.join(query[2:]))

            elif instruction == 'insert':
                self.preparing_insert = True
                self.query(' '.join(query[1:]))
                return

            elif instruction == 'values':
                if self.preparing_insert:
                    self.insert(*query[1:])
                    self.preparing_insert = False
                self.query(' '.join(query[1:]))
                return

            elif instruction == 'where':
                if self.where_clause:
                    error.ClauseErrorMessage('SELECT', 'WHERE')
                    return
                self.where_clause = True
                variable_1 = query[1]
                operation = query[2]
                variable_2 = query[3]
                self.where(variable_1, operation, variable_2)
                self.query(' '.join(query[4:]))

            elif instruction == 'template':
                self.template(*query[1:])

            elif instruction == "and":
                if not self.where_clause:
                    error.ClauseErrorMessage('WHERE', 'AND')
                    return
                variable_1 = query[1]
                operation = query[2]
                variable_2 = query[3]
                self.where(variable_1, operation, variable_2)
                self.query(' '.join(query[4:]))

            elif instruction == 'set':
                self.set(query[1], query[2])
                self.query(' '.join(query[3:]))

            elif instruction == 'list':
                self.list(query[1])
                self.query(' '.join(query[2:]))
        except IndexError:
            return

        result = self.last_selection
        if printing:
            self.where_clause = False
            results_shown = min(len(result), self.env_variables["MAX_RESULTS_SHOWN"])
            for index in range(results_shown):
                row_str = result[index].value.str_justed_by(
                    self.env_variables["MIN_VALUE_LENGTH_SHOWN"])
                row = row_str.replace("'", "")
                
                print(f"{index}: {row[1:-1]}".replace('"', "'"))
            results_shown_text = f"{results_shown} results shown"
            results_hidden_text = f"{len(result) - results_shown} results hidden"
            print(max(len(results_shown_text), len(results_hidden_text)) * "-")
            print(results_shown_text)
            if len(result) > results_shown:
                print(results_hidden_text)

    def select(self, number: int | str) -> None:
        result = self.iter(
            (lambda node, index: node)
        )
        if number == '*':
            self.last_selection = result[1:]
            return
        self.last_selection = result[1:int(number) + 1]

    def set(self, variable: str, value: str) -> None:
        if variable.upper() in self.env_variables:
            value = numberize(value)
            self.env_variables[variable.upper()] = value

    def template(self, *args) -> None:
        self.root.value = Row(*args)
        print(self.root.value)

    def where(self, variable_1: str, operation: str, variable_2: str) -> list:
        result = []
        for row in self.last_selection:
            index_1 = self.root.value.index(variable_1)
            index_2 = self.root.value.index(variable_2)
            if index_1 is None:
                value_1 = variable_1
            else:
                value_1 = row.value[index_1]
            if index_2 is None:
                value_2 = variable_2
            else:
                value_2 = row.value[index_2]

            value_1 = numberize(value_1)
            value_2 = numberize(value_2)
            
            try:
                if operation == '=':
                    if value_1 == value_2:
                        result.append(row)
                elif operation == '>':
                    if value_1 > value_2:
                        result.append(row)
                elif operation == '<':
                    if value_1 < value_2:
                        result.append(row)
                elif operation == '>=':
                    if value_1 >= value_2:
                        result.append(row)
                elif operation == '<=':
                    if value_1 <= value_2:
                        result.append(row)
                elif operation == '!=':
                    if value_1 != value_2:
                        result.append(row)
            except TypeError:
                error.TypeErrorMessage(value_1, operation, value_2)
                return
        self.last_selection = result


class Row(LinkedList):

    def __init__(self, *args) -> None:
        super().__init__()
        for arg in args:
            arg = numberize(arg)
            if type(arg) == str:
                if "\"" in arg or "\'" in arg:
                    arg = arg.replace("'", "").replace('"', '')
                else:
                    continue
            self.append(arg)

    def str_justed_by(self, value) -> str:
        results = self.iter(
            (lambda node, index: repr(node.value).ljust(value).replace("'", '"')),
            (lambda node, node_index: False)
        )
        result = str(results)
        return result.replace(",", " |").replace("[", "").replace("]", "")

    @property
    def root(self) -> Node:
        return self.head
