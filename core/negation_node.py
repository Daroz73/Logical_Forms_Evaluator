from core.node import Node

class Negation_Node(Node):
    def __init__(self, operando:Node):
        self.operando:Node = operando

    def get_variables(self):
        return self.operando.get_variables()
    
    def evaluate(self, evalation):
        return not self.operando.evaluate(evalation)
    
    def __repr__(self):
        return f"!{self.operando.__repr__()}"