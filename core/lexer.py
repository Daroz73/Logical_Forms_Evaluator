from enum import Enum, auto

class TokenType(Enum):
    # operanthors
    VARIABLE = auto()
    CONST = auto()
    # operators
    NOT = auto()
    AND = auto()
    OR = auto()
    IMPLIES = auto()
    IFF = auto()
    # separators
    OPAREN = auto()
    CPAREN = auto()

    ERROR = auto()

    EOF = auto()

class Token:
    def __init__(self, value:str, kind:TokenType):
        self.value:str = value
        self.kind:TokenType = kind
        
    def __repr__(self):
        return f"Token( {self.kind.name}, {self.value} )"

class Lexer:
    def __init__(self, expre:str):
        self.tokens:list[Token] = []
        self.expre = expre
        self.index = 0
        self.tokinize()

    def pop(self)->str:
        if self.index < len(self.expre):
            val = self.expre[self.index]
            self.index += 1
            return val
        else:
            return None
        
    def tokinize(self):
        c_char = self.pop()

        while(c_char):
            if c_char == " " or c_char == "":
                c_char = self.pop()
                continue
            elif c_char.isalpha() and c_char.islower():
                self.tokens.append(Token(c_char, TokenType.VARIABLE))
            elif c_char.isdigit() and (int(c_char) == 0 or int(c_char) == 1):
                self.tokens.append(Token(c_char, TokenType.CONST))
            elif c_char == "=":
                if self.expre[self.index] == ">":
                    val = c_char + self.expre[self.index]
                    self.index += 1
                    self.tokens.append(Token(val, TokenType.IMPLIES))
                else:
                    self.tokens.append(Token(self.expre[self.index], TokenType.ERROR))
            elif c_char == "<":
                if self.expre[self.index] == "=" and self.expre[self.index + 1] == ">":
                    val = c_char + self.expre[self.index] + self.expre[self.index + 1]
                    self.index += 2
                    self.tokens.append(Token(val, TokenType.IFF))
                else:
                    self.tokens.append(Token(c_char, TokenType.ERROR))
            elif c_char == "!":
                self.tokens.append(Token(c_char, TokenType.NOT))
            elif c_char == "&":
                self.tokens.append(Token(c_char, TokenType.AND))
            elif c_char == "|":
                self.tokens.append(Token(c_char, TokenType.OR))
            elif c_char == "(":
                self.tokens.append(Token(c_char, TokenType.OPAREN))
            elif c_char == ")":
                self.tokens.append(Token(c_char, TokenType.CPAREN))                             
            else:
                self.tokens.append(Token(c_char, TokenType.ERROR))
            c_char = self.pop()
        self.tokens.append(Token(" ",TokenType.EOF))