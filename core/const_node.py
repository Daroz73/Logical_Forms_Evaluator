from core.node import Node

class Const_Node(Node):
    def __init__(self, simb:str):
        self.simb = simb
        self.value = True if self.simb == "1" else False
    
    def get_variables(self):
        return {self.simb}

    def evaluate(self, evaluation:dict[str, bool]) -> bool:
        return self.value

    def __repr__(self):
        return self.simb
        