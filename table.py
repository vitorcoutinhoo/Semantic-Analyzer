# pylint: disable = C0303, C0114, C0115, C0116

# Author: Vítor Coutinho
# Arquive to build the symbol table

class Table:
    def __init__(self):
        self.content = []
    
    def add(self, tk, lex, tp, value):
        # adiciona uma declaração na tabela
        self.content.append([tk, lex, tp, value])
    
    def update(self, lex, tp, value):
        # atualiza o tipo e o valor de um lexema
        for row in self.content:
            if row[1] == lex:
                row[2] = tp
                row[3] = value
                break

    def remove(self, lex):
        for row in self.content:
            if row[1] == lex:
                # remove uma declaração da tabela
                self.content.remove(row)
                break

    def show(self):
        header = ('-'*31 + "\n" 
                + ' '*2 + "Tk" + ' '*4 + "Lex" + ' '*5 + "Type" + ' '*4 + "Value" + ' '*2 + "\n" 
                + '-'*31 + "\n")

        body = []
        for row in self.content:
            # printa cada declaração da tabela
            body.append(f"{row[0]:>4}{row[1]:>7} {row[2]:>8} {row[3]:>8}")
        
        res = header + "\n".join(body)
        print(res + "\n" + '-'*31 + "\n")