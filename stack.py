# pylint: disable = C0303, C0114, C0116, C0115

# Author: Vítor Coutinho
# Arquive to build the stack of scopes

from table import Table

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, scope: Table):
        # insere um escopo na pilha
        self.stack.insert(0, scope)

    def pop(self):
        # remove o escopo da pilha
        return self.stack.pop(0)

    def copy(self):
        # retorna uma cópia da pilha
        return self.stack[-1]

    def search(self, lex: str):
        # copia a pilha
        copy = self.stack.copy()
        while copy:
            # da pop na pilha até achar o escopo que contém o lexema
            scope = copy.pop(0)
            
            for row in scope.content:
                if lex in row:
                    return row[3] # retorna o valor do lexema
            
        return None

    def show(self):
        # printa cada escopo da pilha
        for scope in self.stack:
            scope.show()
        