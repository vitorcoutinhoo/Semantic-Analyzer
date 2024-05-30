# pylint: disable = C0303, C0114

# Author: Vítor Coutinho
# Arquive to build the stack of scopes

from table import Table

class Stack:
    """
        A class to represent a stack of scopes.

        Attributes:
            stack (list): A list of Table objects.
    """
    def __init__(self):
        self.stack = []
    
    def push(self, scope: Table):
        """
            Add a new scope to the stack.
        """
        self.stack.append(scope)

    def pop(self):
        """
            Remove the top scope from the stack.
        """
        return self.stack.pop()

    def copy(self):
        """
            Return a copy of the top scope.
        """
        return self.stack[-1]

    def search(self, lex: str):
        """
            Search for a lexeme in the top scope.

            Args:
                lex (str): The lexeme to be searched.

            Returns:
                The entire row of the lexeme.
        """
        scope = self.pop()

        for row in scope.content:
            if row[1] == lex:
                return row
            
        return None