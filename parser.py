from lexer import *
from negation_node import Negation_Node
from implies_node import Implies_Node
from iff_node import IFF_Node
from disyunction_node import Disyunction_Node
from conjunction_node import Conjunction_Node
from error_node import Error_Node
from node import Node
from node_atom import Node_Atom
from paren_node import Paren_Node

class Parser:
    def __init__(self, form:str):
        self._pos = 0
        self._tokens = Lexer(form).tokens
        self.AST:Node = self.parsing()

    def parsing(self) -> Node:
        if self._current_token().kind == TokenType.EOF:
            raise Error_Node("Void Formula", "La entrada esta vacia se esperaba una formula")
        
        left = self._parse_iff()

        if self._current_token().kind != TokenType.EOF:
            raise Error_Node("Syntaxis Error", "Se esperaba que la formula se terminara")

        return left

    def _parse_iff(self) -> Node:
        left = self._parse_implies()

        while self._current_token().kind == TokenType.IFF:
            self._next_token()
            right = self._parse_implies()
            left = IFF_Node(left, right)
        
        return left 


    def _parse_implies(self) -> Node:
        left = self._parse_disyuntion()

        while self._current_token().kind == TokenType.IMPLIES:
            self._next_token()
            right = self._parse_disyuntion()
            left = Implies_Node(left, right)
        
        return left


    def _parse_disyuntion(self) -> Node:
        left = self._parse_conjuntion()

        while self._current_token().kind == TokenType.OR:
            self._next_token()
            right = self._parse_conjuntion()
            left = Disyunction_Node(left, right)
        
        return left


    def _parse_conjuntion(self) -> Node:
        left = self._parse_negation()

        while self._current_token().kind == TokenType.AND:
            self._next_token()
            right  = self._parse_conjuntion()
            left = Conjunction_Node(left, right)
        
        return left
            

    def _parse_negation(self) -> Node:        
        counter = 0
        while self._current_token().kind == TokenType.NOT:
            self._next_token()
            counter += 1
        operator = self._current_token()
        if counter % 2 == 0 and (operator.kind == TokenType.OPAREN or operator.kind == TokenType.VARIABLE or operator.kind == TokenType.NUMBER):
            operator = self._parse_atom()
        elif operator.kind == TokenType.NUMBER or operator.kind == TokenType.VARIABLE or operator.kind == TokenType.OPAREN:
            operator = Negation_Node(self._parse_atom())
        else:
            raise Error_Node("Syntaxi Error", "Se esperaba una variable o expresion")

        return operator


    def _parse_atom(self) -> Node:
        atom = self._current_token()
        if atom.kind == TokenType.VARIABLE or atom.kind == TokenType.NUMBER:
            self._next_token()
            return Node_Atom(atom)
        elif atom.kind == TokenType.OPAREN:
            self._next_token()
            atom = self._parse_iff()
            if self._current_token().kind == TokenType.CPAREN:
                self._next_token()
                return Paren_Node(atom)
            else:
                raise Error_Node("Not closed Paren", "Se esperaba que cerraras el parentesis")
        else:
            raise Error_Node("Invalid Expression", "No se reconoce la expresion usada")

    def _current_token(self) -> Token:
        if self._pos < len(self._tokens):
            return self._tokens[self._pos]
        return None
        
    
    def _pop(self) -> Token:
        if self._pos < len(self._tokens):
            tk = self._tokens[self._pos]
            self._pos += 1
            return tk
        return None
    
    def _next_token(self):
        self._pos+=1