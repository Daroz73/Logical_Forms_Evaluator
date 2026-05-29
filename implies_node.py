from node import Node

class Implies_Node(Node):
    def __init__(self, left:Node, right:Node):
        self.left:Node = left
        self.right:Node = right
    
    def get_variables(self) -> set[str]:
        return self.left.get_variables() | self.right.get_variables()
    
    def evaluate(self, evalation:dict[str, bool]) -> bool:
        return not self.left.evaluate(evalation) or self.right.evaluate(evalation)
    
    def __repr__(self):
        return f"{self.left.__repr__()} => {self.right.__repr__()}"