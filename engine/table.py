import re, sys
from typing import List

import core.error as error
from core.graph import Graph
from core.node import Node
from core.utils import numberize
from engine.row import DataRow


class DataTable(Graph):

    def __init__(self, name = "MainTable") -> None:
        super().__init__()
        self.name = name
        self.root = Node(DataRow())
        self.preparing_insert = False
        self.preparing_update = False
        self.preparing_order_index = None
        self.where_clause = False
        self.last_selection: List[Node] = []
        self.env_variables = {
            "MAX_RESULTS_SHOWN": 10,
            "MIN_VALUE_LENGTH_SHOWN": 17,
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
            "SET",
            "LIKE",
            "ORDER",
            "BY",
            "UPDATE"
        ]
        self.defined_clauses.sort()

    def insert(self, *args) -> None:
        self.append(self.root.id, DataRow(*args))

    def list(self, clause: str) -> None:
        if clause == 'env':
            print(*list(self.env_variables.keys()), sep = "\n")
        elif clause == 'clauses':
            print(*self.defined_clauses, sep = "\n")
        else:
            error.UndefinedClauseErrorMessage(clause)

    def load_from_csv(self, csv: str) -> None:
        for line in csv.splitlines():
            line = line.strip()
            if line == '':
                continue
            raw_row = line.split(",")
            row = [value.strip() for value in raw_row]
            self.insert(*row)

    def order(self, column_name: str) -> None:
        if column_name not in self.root.value:
            print("Column name not in template: ")
            return self.template()
        self.preparing_order_index = self.root.value.index(column_name)

    def order_by(self, method: str) -> None:
        index  =self.preparing_order_index
        key = lambda node: node.value[index]
        if method == "ASC":
            self.last_selection.sort(key = key)
        elif method == "DESC":
            self.last_selection.sort(key = key, reverse = True)

    def print_results(self, results: list, identation_level: int = 0) -> None:
        identation = identation_level * "    "
        results_shown = min(len(results), self.env_variables["MAX_RESULTS_SHOWN"])
        for index in range(results_shown):
            row_node: Node = results[index]
            raw_row: DataRow = row_node.value
            row_str = raw_row.str_justed_by(
                self.env_variables["MIN_VALUE_LENGTH_SHOWN"])
            row = row_str.replace("'", "")
            print(identation + f"{index}: {row}".replace('"', "'").strip())
        results_shown_text = f"{results_shown} results shown"
        results_hidden_text = f"{len(results) - results_shown} results hidden"
        print(identation + max(len(results_shown_text), len(results_hidden_text)) * "-")
        print(identation + results_shown_text)
        if len(results) > results_shown:
            print(identation + results_hidden_text)

    def query(self, query: str) -> None:
        printing = query.endswith(';')
        if printing:
            query = query[:-1]
        query = query.split()
        if len(query) == 0:
            return
        instruction = query[0].lower()

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
                elif self.preparing_update:
                    self.update(*query[1:])
                    self.preparing_update = False
                return

            elif instruction == 'where':
                if self.where_clause:
                    error.ClauseSyntaxErrorMessage('SELECT', 'WHERE')
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
                    error.ClauseSyntaxErrorMessage('WHERE', 'AND')
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

            elif instruction == "order":
                self.order(query[1])
                self.query(' '.join(query[2:]))

            elif instruction == "by":
                if self.preparing_order_index is not None:
                    self.order_by(query[1].upper())
                    self.preparing_order_index = None
                self.query(' '.join(query[2:]))

            elif instruction == "update":
                self.preparing_update = True
                self.query(' '.join(query[1:]))

            else:
                pass

        except IndexError:
            return

        result = self.last_selection
        if printing:
            self.where_clause = False
            self.print_results(result)

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
            print(f"ENV {variable.upper()} <- {value}")

    def template(self, *args) -> None:
        if len(args) > 0:
            self.root.value = DataRow(*args)
        print(self.root.value)

    def update(self, *args) -> None:
        if len(args) != len(self.root.value):
            error.ArgumentNumberErrorMessage('UPDATE', len(self.root.value), len(args))
            return
        for row in self.last_selection:
            row.value = DataRow(*args)

    def where(self, variable_1: str, operation: str, variable_2: str) -> list:
        result = []
        for row in self.last_selection:
            index_1 = self.root.value.index(variable_1)
            if index_1 is None:
                value_1 = variable_1
            else:
                value_1 = row.value[index_1]

            index_2 = self.root.value.index(variable_2)
            if index_2 is None:
                value_2 = variable_2
            else:
                value_2 = row.value[index_2]

            value_1 = numberize(value_1)
            value_2 = numberize(value_2)
            operation = operation.upper()

            if type(value_1) == str:
                value_1 = value_1.strip().strip("'").strip('"')
            if type(value_2) == str and operation != "LIKE":
                value_2 = value_2.strip().strip("'").strip('"')

            try:
                if operation == '=':
                    condition =  value_1 == value_2
                elif operation == '>':
                    condition =  value_1 > value_2
                elif operation == '<':
                    condition =  value_1 < value_2
                elif operation == '>=':
                    condition =  value_1 >= value_2
                elif operation == '<=':
                    condition = value_1 <= value_2
                elif operation == '!=':
                    condition = value_1 != value_2
                elif operation == "LIKE":
                    condition = re.match(value_2, value_1)
                else:
                    condition = False

                if condition:
                    result.append(row)
            except TypeError:
                error.TypeErrorMessage(value_1, operation, value_2)
                return
        self.last_selection = result
