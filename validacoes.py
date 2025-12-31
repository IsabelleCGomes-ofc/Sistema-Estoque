#validar número e valores vazios
from data import salvarProduto

#----------------achar produto-----------------------------------------------------
def encontrarProduto(encontrado, estoque):

    if not encontrado:
        print("Produto não encontrado :/\n")

#---------------inteiros------------------------------------------------------------
def validarInteiro():

    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))

            if quantidade <= 0:
                print("O valor digitado precisa ser positivo. Tente novamente!")
                continue

            return quantidade


        except ValueError:
            print("Quantidade precisa ser número inteiro")

#-------------texto-------------------------------------------------------------------
def validarTexto():
    while True:
        texto = input("Digite o nome: ")

        if not texto.strip():
            print("O texto não pode ficar vazio. Tente novamente!")
            continue
        return texto

#--------------quebrados--------------------------------------------------------------
def validarReal():

    while True:
        try:
            valor = float(input("Digite o valor: "))

            if valor <= 0:
                print("O valor digitado precisa ser positivo. Tente novamente!")
                continue

            return valor

        except ValueError:
            print("valor precisa ser número real positivo. Tente novamente!")

#-----------------validar ID------------------------------------------------------------
def validarID():
    while True:
        id = input("Digite o id do produto: ")

        if id.strip() == "":
            print("o id não pode ficar vazio. Tente novamente!")
            continue

        try:
            id = int(id)

        except ValueError:
            print("ID deve ser número inteiro. Tente novamente!")
            continue

        if id < 0:
            print("ID deve ser positivo. Tente novamente!")
            continue

        return id