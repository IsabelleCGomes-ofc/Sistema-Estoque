import json
import os

from utils import limpar_tela

ARQUIVO = "estoque.json"

if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w") as arquivo:
        json.dump([], arquivo, indent=4)

#exibir menu
while True:
    limpar_tela()
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Entrada de estoque")
    print("4 - Saída de estoque")
    print("5 - Remover produto")
    print("0 - Sair")
    opcao = input("Escolha uma opcao: ")

    if opcao == 1:
        #funcao limpar tela
        #cadastro
        with open(ARQUIVO, "r") as arquivo:
            json.dump([], arquivo, indent=4)
            lista = json.load(arquivo)
        input("Aperte 'enter' para finalizar... ")
    elif opcao == 2:
        #funcao limpar
        #exibir produtos do estoque
        print("Aqui aparece os produtos!")
        input("Aperte 'enter' para finalizar...")
    elif opcao == 3:
        #funcao limpar
        #receber quantidade de produto que chegou e somar
        quantidadeSomada = int(input("Digite a quantidade recebida do produto: "))
        # verificar se é número
        input("Aperte 'enter' para finalizar...")
    elif opcao == 4:
        #funcao limpar
        #receber quantidade do produto que saiu e subtrair
        quantidadeSaida = int(input("Digite a quantidade saída do produto: "))
        #verificar se é número
        input("Aperte 'enter' para finalizar...")
    elif opcao == 5:
        #funcao limpar
        #receber o id do produto a remover
        #apagar aquele produto da lista
        idDelete = input("Digite o id do produto que deseja remover: ")
        #verificar se esse id existe
        input("Aperte 'enter' para finalizar...")
    elif opcao == 0:
        #funcao limpar
        #sair
        print("Finalizando...")
        break
    else:
        input("A opção que você escolheu não existe! Aperte 'enter' e tente novamente.")
#limpar menu

#verificar qual a opção selecionada

#chamar functions ou fazer entrada e saída de dados aqui


