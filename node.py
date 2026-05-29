from abc import ABC


class Node(ABC):
    @staticmethod
    def get_variables(self) -> set[str]:
        pass

    @staticmethod
    def evaluate(self, evalation:dict[str, bool]) -> bool:
        pass

    @staticmethod
    def __repr__(self):
        pass