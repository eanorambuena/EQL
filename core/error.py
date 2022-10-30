class IdError(Exception):
    def __init__(self, id: int) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"Node with id {self.id} not found in graph"
 

class ClauseErrorMessage():
    def __init__(self, clause: str, instruction: str) -> None:
        self.clause = clause.upper()
        self.instruction = instruction.upper()
        print("ClauseError:", self)

    def __str__(self) -> str:
        return f"{self.instruction} used before {self.clause} clause"


class TypeErrorMessage():
    def __init__(self, value_1, operation: str, value_2) -> None:
        self.value_1 = value_1
        self.operation = operation
        self.value_2 = value_2
        print("TypeError:", self)

    def __str__(self) -> str:
        return f"{self.value_1} {self.operation} {self.value_2} is not a valid operation"