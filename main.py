# pylint: disable = C0303, C0114, C0200, W0621, W0612, C0103, C0116

# Author: Vítor Coutinho
# Method: An Stack of scopes

from table import Table
from stack import Stack
from arquive import read, unifylist

# pilha de escopos
stack = Stack()


# chamado quando aparecer o comando "BLOCO" no codigo
def bloco(nome: str):
    bloco = Table(nome)
    return bloco  # retorna o bloco criado


# chamado quando aparecer o comando "FIM" no codigo
def fim():
    stack.pop()  # desempilha o bloco atual


# verifica o tipo do valor
def value_type(value):
    # verifica se é uma cadeia
    if '"' in value:
        return "CADEIA"

    # verifica se é um número
    if value.isdigit() or any(char in value for char in [".", "+", "-"]):
        return "NUMERO"

    return None


# verifica se é uma variável
def is_variable(value):
    if (
        value
        not in [
            "CADEIA",
            "NUMERO",
            "BLOCO",
            "FIM",
            "PRINT",
        ]  # se não for uma palavra reservada
        and value[0].isalpha()  # se a primeira letra for uma letra
    ):
        return True
    return False


# processa a linha do código
def process_row(row, data_type, initial_value):
    size = len(row)  # tamanho da linha

    for i in range(1, size):  # percorre a linha
        if is_variable(row[i]):
            if stack.top().search(row[i]) is not None:  # se a variável já foi declarada
                stack.top().update(
                    row[i], data_type, initial_value
                )  # atualiza o valor da variável
            else:
                stack.top().add(
                    "ID", row[i], data_type, initial_value
                )  # adiciona a variável na tabela

        if row[i] == "=":
            if value_type(row[i + 1]) == data_type:
                stack.top().update(
                    row[i - 1], data_type, row[i + 1]
                )  # atualiza o valor da variável


# reconhece os comandos do código
def recognize_commands(row, linha: int):
    # ignora linhas em branco
    if row == [] or row[0] == "\n":
        return

    # cria um novo bloco na pilha
    if row[0] == "BLOCO":
        stack.push(bloco(row[1]))

    # fecha o bloco atual e desempilha
    if row[0] == "FIM":
        if stack.top().name == row[1]:
            fim()
        else:
            print(f"Erro na linha {linha}: bloco não encontrado")

    # se for uma cadeia
    if row[0] == "CADEIA":
        process_row(row, "CADEIA", '""')

    # se for um número
    if row[0] == "NUMERO":
        process_row(row, "NUMERO", 0)

    # atribuição de variáveis
    if is_variable(row[0]):
        table = stack.search(row[0])

        # se a variável não foi declarada
        if table is None:
            print(f"Erro na linha {linha}: variável não declarada")
            return

        # se for variavel = variavel
        if is_variable(row[2]):
            aux = stack.search(row[2])
            if aux is not None and aux[2] == table[2]:
                stack.update(row[0], aux[2], aux[3])
            else:
                print(f"Erro na linha {linha}: variável não declarada")
        else:
            # se for variavel = valor
            aux = value_type(row[2])
            if aux == table[2]:
                stack.update(row[0], aux, row[2])
            else:
                print(f"Erro na linha {linha}: tipo incompatível")

    # comando PRINT
    if row[0] == "PRINT":
        aux = stack.search(row[1])
        if aux is not None:
            print(aux[3])  # imprime o valor da variável
        else:
            print(f"Erro na linha {linha}: variável não declarada")


def main():
    # caminho do arquivo de entrada
    PATH = "input.txt"

    # arquivo de entrada: lista de listas
    inpt = [unifylist(row) for row in read(PATH)]

    linha = 1
    for row in inpt:
        recognize_commands(row, linha)
        linha += 1


main()
