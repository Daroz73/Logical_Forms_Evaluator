from core.node import Node

class Paren_Node(Node):
    def __init__(self, operando:Node):
        self.operando:Node = operando
    
    def get_variables(self) -> set[str]:
        return self.operando.get_variables()
    
    def evaluate(self, evalation:dict[str, bool]) -> bool:
        return self.operando.evaluate(evalation)

    def unwrap(self) -> Node:
        if isinstance(self.operando, Paren_Node):
            return self.operando.unwrap()
        return self.operando

    def __repr__(self):
        return f"({self.operando.__repr__()})"