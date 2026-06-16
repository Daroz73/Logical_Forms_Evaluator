from core.parser import Parser

class Evaluator:
    def __init__(self, form:str):
        self.ast = Parser(form).AST
        self._evaluator:dict[str,bool] = {var:False for var in self.ast.get_variables()}
        self._cases:list[tuple[dict[str,bool], bool]] = []
        self._was_True = 0
        self._was_False = 0
        self._evaluate(0, list(self.ast.get_variables()), [False for _ in self.ast.get_variables()])
        self.is_tautology:bool = True if self._was_True == 2**len(self._evaluator.keys()) else False
        self.is_contradiction:bool = True if self._was_False == 2**len(self._evaluator.keys()) else False
        self.is_contingency: bool =  not(self.is_tautology or self.is_contradiction)


    def _evaluate(self, index:int, vars:list[str], mask:list[bool]):
        if index == len(vars):
            return

        if not mask[index]:
            mask[index] = True
            self._evaluator[vars[index]] = True
            if self.ast.evaluate(self._evaluator):
                self._was_True += 1
                self._cases.append((self._evaluator.copy(), True))
            else:
                self._was_False += 1
                self._cases.append((self._evaluator.copy(), False))
            
            self._evaluate(index+1, vars, mask)

            self._evaluator[vars[index]] = False
            mask[index] = False        
            if self.ast.evaluate(self._evaluator):
                self._was_True += 1
                self._cases.append((self._evaluator.copy(), True))
            else:
                self._was_False += 1
                self._cases.append((self._evaluator.copy(), False))


    def veritative_table(self) -> str:
        table:str = ""
        vars = list(self.ast.get_variables())
        for v in vars:
            table += f"| {v} "
        table += "|" + self.ast.__repr__()+ "|\n"

        for t in self._cases:
            for i in range(len(vars)):
                table += f"| {"T" if t[0][vars[i]] else "F"} "
            table += f"| {t[1]} |\n"

        if self.is_tautology:
            table += f"| tautology | {self.is_tautology}"
        elif self.is_contradiction:
            table += f"| contradiction | {self.is_contradiction}"
        else:
            table += f"| contingency | {self.is_contingency}"

        return table  