# pylint: disable = C0303, C0114

# Author: Vítor Coutinho
# Arquive to build the symbol table

class Table:
    """
        A class to represent a symbol table.

        Attributes:
            content (list): A list of lists, where each list is a row of the table.
    """

    def __init__(self):
        self.content = []
    
    def add(self, tk, lex, tp, value):
        """
            Add a new lexeme to the table.

            Args:
                tk (int): The token of the lexeme.
                lex (str): The lexeme to be added.
                type (str): The type of the lexeme.
                value (str): The value of the lexeme.
        """
        self.content.append([tk, lex, tp, value])
    
    def update(self, lex, tp, value):
        """
            Update the type and value of a lexeme in the table.

            Args:
                lex (str): The lexeme to be updated.
                type (str): The new type of the lexeme.
                value (str): The new value of the lexeme.
        """
        for row in self.content:
            if row[1] == lex:
                row[2] = tp
                row[3] = value
                break

    def remove(self, lex):
        """
            Remove a lexeme from the table.

            Args:
                lex (str): The lexeme to be removed.
        """
        for row in self.content:
            if row[1] == lex:
                self.content.remove(row)
                break

    def show(self):
        """
            Print the table in a formatted way.
        """
        header = ('-'*31 + "\n" 
                + ' '*2 + "Tk" + ' '*4 + "Lex" + ' '*5 + "Type" + ' '*4 + "Value" + ' '*2 + "\n" 
                + '-'*31 + "\n")

        body = []
        for row in self.content:
            body.append(f"{row[0]:>4}{row[1]:>7} {row[2]:>8} {row[3]:>8}")
        
        res = header + "\n".join(body)
        print(res + "\n" + '-'*31 + "\n")