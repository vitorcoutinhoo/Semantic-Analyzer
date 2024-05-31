# pylint: disable = C0303, C0114, C0200, W0621, C0116

# Author: Vítor Coutinho
# Functions for reading the file


def read(file):
    string = []
    
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()

        # retira as linhas vazias
        for line in lines:
            if line != "\n":
                string.append(line.strip(" \n\t").split(" ", 1))

        # separa os elementos de cada linha
        for row in string:
            for i in range(len(row)):

                # separa por vírgula
                if "," in row[i]:
                    row[i] = row[i].split(",")
                    row[i] = [x.strip() for x in row[i]]

                # separa por igual
                if "=" in row[i]:
                    row[i] = row[i].split("=")
                    row[i] = [x.strip() for x in row[i]]

                # separa lista de lista
                if isinstance(row[i], list):
                    for j in range(len(row[i])):
                        if "=" in row[i][j]:
                            row[i][j] = row[i][j].split("=")
                            row[i][j] = [x.strip() for x in row[i][j]]

    return string


def unifylist(lst):
    result = []

    for item in lst:
        # junta todas as listas em uma só
        if isinstance(item, list):
            result.extend(unifylist(item)) 
        else:
            if item != "":
                result.append(item)
    return result
