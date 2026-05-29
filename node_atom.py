from node import Node
from lexer import Token

class Node_Atom(Node):
    def __init__(self, tk:Token):
        self.name = tk.value

    def get_variables(self) -> set[str]:
        return {self.name}

    def evaluate(self, evaluation:dict[str, bool]) -> bool:
        return evaluation[self.name]

    def __repr__(self):
        return self.name