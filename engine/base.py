import sys
from types import NoneType

import core.error as error
from core.graph import Graph
from core.node import Node
from engine.table import DataTable


class DataBase(Graph):

    def __init__(self, name = "MainDataBase") -> None:
        super().__init__()
        self.root = Node(DataTable())
        self.current_table = None
        self.global_variables = {
            "NAME": name
        }
        self.defined_clauses = list(set([
            "CHECKOUT",
            "LIST",
            "TABLES",
            "EXIT",
            "CLAUSES",
            "LET",
            ";;" # Print last selection
        ] + self.root.value.defined_clauses))
        self.defined_clauses.sort()

    def create_table(self, name) -> bool:
        return self.append(self.root.id, DataTable(name))

    def list_tables(self) -> None:
        results = self.iter(
            (lambda node, index: node.value.name),
            (lambda node, index: False)
        )
        print(*results, sep = "\n")

    @property
    def name(self) -> str:
        return self.global_variables["NAME"]

    def redirect_query(self, query: str) -> None:
        if self.current_table is None:
            print("No table selected")
        else:
            self.current_table.query(query)

    def query(self, query: str) -> None:
        if len(query) == 0:
            return

        query = query.split()
        instruction = query[0].lower()
        try:
            if instruction == 'exit':
                sys.exit()

            elif instruction == "checkout":
                self.current_table = self.use_table(query[1])
                self.query(" ".join(query[2:]))

            elif instruction == "list":
                if query[1].lower() == "tables":
                    self.list_tables()
                    self.query(" ".join(query[2:]))
                elif query[1].lower() == "clauses":
                    print(*self.defined_clauses, sep = "\n")
                    self.query(" ".join(query[2:]))
                else:
                    self.redirect_query(" ".join(query))

            elif instruction == "let":
                if query[2] != "*":
                    self.global_variables[query[1].upper()] = query[2]
                    print(f"{query[1].upper()} <- {query[2]}")
                elif self.current_table is None:
                    print("No table selected")
                else:
                    self.global_variables[query[1].upper()] = self.current_table.last_selection
                    print(f"{query[1].upper()} <- (")
                    self.current_table.print_results(self.current_table.last_selection, 1)
                    print(")")
                
            elif instruction.upper() in self.defined_clauses:
                self.redirect_query(" ".join(query))

            else:
                error.UndefinedClauseErrorMessage(instruction)

        except IndexError:
            return

    def use_table(self, name) -> DataTable | NoneType:
        if name == "MainTable":
            return self.root.value
        results = self.iter(
            (lambda node, index: node),
            (lambda node, index: node.value.name == name)
        )
        if results[-1].value.name == name:
            return results[-1].value
        return self.current_table