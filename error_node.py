from lexer import Token
from node import Node

class Error_Node(Node):
    def __init__(self, kind:str, description:str):
        self.kind:str = kind
        self.description:str = description
    
    def get_variables(self):
        return set([])

    def evaluate(self, evalation):
        return False

    def __repr__(self):
        return f"{self.kind}: {self.description}"