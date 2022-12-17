import pickle, re, sys
from types import NoneType
from typing import List 

import core.error as error
from core.graph import Graph
from core.node import Node
from engine.row import DataRow
from engine.table import DataTable


class DataBase(Graph):

    def __init__(self, path: str, name = "MainDataBase") -> None:
        super().__init__()
        self.root = Node(DataTable())
        self.current_table = None
        self.path = path
        self.global_variables = {
            "NAME": name,
        }
        self.defined_clauses = list(set([
            "CHECKOUT",
            "LIST",
            "TABLES",
            "EXIT",
            "CLAUSES",
            "LET",
            "GET",
            "CREATE",
            "DROP",
            "GLOBAL",
            "BIND",
            "AS",
            "ECHO",
            ";;"
        ] + self.root.value.defined_clauses))
        self.defined_clauses.sort()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.save()

    def bind(self, *table_names) -> None:
        nicks = []
        if "AS" in table_names:
            as_index = table_names.index("AS")
            if 0 < as_index < len(table_names) - 1:
                nicks = table_names[as_index + 1:]
                table_names = table_names[:as_index]

        tables: List[DataTable] = []
        for table_name in table_names:
            if not self.check_table(table_name):
                return
            table = self.use_table(table_name)
            table.select("*")
            tables.append(table)
            
        selections: List[List[Node]] = [table.last_selection for table in tables]
        selection_sizes = list(map(len, selections))
        if min(selection_sizes) != max(selection_sizes):
            print(f"Tables {', '.join(table_names)} must have the same number of rows")
            return

        template = []
        for table_index in range(len(tables)):
            table = tables[table_index]
            nick = table.name
            if table_index < len(nicks):
                nick = nicks[table_index]
            
            for index in range(len(table.root.value)):
                item = table.root.value[index]
                template.append(f"'{nick}${item}'")
        self.current_table.template(*template)

        for row_index in range(selection_sizes[0]):
            items = []
            for selection in selections:
                row = selection[row_index].value
                for index in range(len(row)):
                    item = row[index]
                    if type(item) == str:
                        item = f"'{item}'"
                    items.append(item)
            self.current_table.insert(*items)

    def check_table(self, name: str) -> bool:
        if name not in self.list_tables(False):
            print(f"Table {name} does not exist\nCurrent tables:")
            self.list_tables()
            return False
        return True

    def create_table(self, name) -> bool:
        return self.append(self.root.id, DataTable(name))

    def drop_table(self, name: str) -> None:
        if name == "MainTable":
            print("Cannot drop MainTable")
            return
        if not self.check_table(name):
            return
        table = self.use_table(name)
        if self.current_table == table:
            self.current_table = None
        id = self.id(table)
        self.root.pointers.pop(id)

    def get_parents(self, id: int) -> list:
        return [self.root]

    def list_tables(self, printing = True) -> list:
        results = self.iter(
            (lambda node, index: node.value.name),
            (lambda node, index: False)
        )
        if printing:
            print(*results, sep = "\n")
        return results

    @property
    def name(self) -> str:
        return self.global_variables["NAME"]

    def parse_expression(self, value: str) -> str:
        return value

    def redirect_query(self, query: str) -> None:
        if self.current_table is None:
            print("No table selected")
        else:
            self.current_table.query(query)

    def save(self) -> None:
        with open(self.path, "wb") as file:
            pickle.dump(self, file)
        print(f"Database {self.name} saved to {self.path}")

    def query(self, query: str) -> None:
        if len(query) == 0:
            return

        query = query.split()
        if len(query) == 0:
            return

        instruction = query[0].lower()
        try:
            if instruction == 'exit':
                self.save("database.edb")
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
                elif query[1].lower() == "global":
                    print(*self.global_variables, sep = "\n")
                    self.query(" ".join(query[2:]))
                else:
                    self.redirect_query(" ".join(query))

            elif instruction == "let":
                value = self.parse_expression(query[2])
                if value != "*":
                    self.global_variables[query[1].upper()] = value
                    print(f"GLOBAL {query[1].upper()} <- {value}")
                elif self.current_table is None:
                    print("No table selected")
                else:
                    self.global_variables[query[1].upper()] = self.current_table.last_selection
                    print(f"{query[1].upper()} <- (")
                    self.current_table.print_results(self.current_table.last_selection, 1)
                    print(")")

            elif instruction == "get":
                if self.current_table is not None:
                    if query[1].upper() in self.current_table.env_variables:
                        result = self.current_table.env_variables[query[1].upper()]
                        print(f"ENV {query[1].upper()} ->", end = " ")
                    elif query[1].upper() in self.global_variables:
                        result = self.global_variables[query[1].upper()]
                        print(f"GLOBAL {query[1].upper()} ->", end = " ")

                    self.current_table.last_selection = [Node(DataRow(
                        f"'{query[1].upper()}'", f"'{result}'"))]

                    if type(result) == list and len(result) > 0 and type(result[0]) == Node \
                            and type(result[0].value) == DataRow:
                        print("(")
                        self.current_table.print_results(result, 1)
                        print(")")
                    else:
                        print(result)

                elif query[1].upper() in self.global_variables: 
                        print(f"GLOBAL {query[1].upper()} ->",
                            f"{self.global_variables[query[1].upper()]}")

            elif instruction == "create":
                self.create_table(query[1])
                self.query(" ".join(query[2:]))
     
            elif instruction == "drop":
                self.drop_table(query[1])
                self.query(" ".join(query[2:]))

            elif instruction == "bind":
                self.bind(*query[1:])
            
            elif instruction == "echo":
                content = " ".join(query[1:])
                print("\x1b[1;37m", content.replace("\\", "\n"), "\x1b[0;37m")
                
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

def open_database(path: str) -> DataBase:
    if path[-4:] != ".edb":
        print("Invalid database file")
        return None

    with open(path, "rb") as file:
        return pickle.load(file)
