from core.parser import Parser

class Evaluator:
    def __init__(self, form:str):
        self.ast = Parser(form).AST
        self._evaluator:dict[str,bool] = {var:False for var in self.ast.get_variables()}
        self._cases:list[tuple[dict[str,bool], bool]] = []
        self._was_True = 0
        self._was_False = 0
        self._evaluate(0, list(self.ast.get_variables()))
        self.is_tautology:bool = True if self._was_True == 2**len(self._evaluator.keys()) else False
        self.is_contradiction:bool = True if self._was_False == 2**len(self._evaluator.keys()) else False
        self.is_contingency: bool =  not(self.is_tautology or self.is_contradiction)


    def _evaluate(self, index:int, vars:list[str]) -> None:
        if index == len(vars):
            result = self.ast.evaluate(self._evaluator)
            if result:
                self._was_True += 1
            else:
                self._was_False += 1
            self._cases.append((self._evaluator.copy(), result))
            return
        if vars[index] == "1":    
            self._evaluator[vars[index]] = True
            self._evaluate(index+1, vars)
        elif vars[index] == "0":
            self._evaluator[vars[index]] = False
            self._evaluate(index+1, vars)
        else:
            self._evaluator[vars[index]] = True
            self._evaluate(index+1, vars)
            self._evaluator[vars[index]] = False
            self._evaluate(index+1, vars)

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