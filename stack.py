# pylint: disable = C0303, C0114, C0116, C0115

# Author: Vítor Coutinho
# Arquive to build the stack of scopes

from table import Table

class Stack:
    def __init__(self):
        self.stack = []
    
    def size(self):
        # retorna o tamanho da pilha
        return len(self.stack)
    
    def push(self, scope: Table):
        # insere um escopo na pilha
        self.stack.insert(0, scope)

    def pop(self):
        # remove o escopo da pilha
        return self.stack.pop(0)

    def top(self):
        # retorna uma cópia do topo da pilha
        return self.stack[0]

    def search(self, lex: str):
        # copia a pilha
        copy = self.stack.copy()
        while copy:
            # procura o lexema em cada escopo da pilha
            scope = copy.pop(0)
            if scope.search(lex):
                return scope.search(lex)
        
        return None
    
    def update(self, lex: str, tp: str, value: str):
        # atualiza o tipo e o valor de um lexema
        for scope in self.stack:
            if scope.search(lex):
                scope.update(lex, tp, value)
                break

    def show(self):
        # printa cada escopo da pilha
        for scope in self.stack:
            scope.show()
        