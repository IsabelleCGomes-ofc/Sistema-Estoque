import json
import os

from utils import limpar_tela

ARQUIVO = "estoque.json"

def carregarEstoque():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w") as arquivo:
            json.dump([], arquivo, indent=4)

    with open(ARQUIVO, "r") as arquivo:
        estoqueLista = json.load(arquivo)

    return estoqueLista


def gerarId(estoqueLista):
    if len(estoqueLista) == 0: #len=conta quantos elementos tem a variavel, chars, chaves, elementos de lista..
        idPrimário = 1
        return idPrimário
    else:
        ids = [item["id"] for item in estoqueLista] #obs: item é comando de lista
        id = max(ids) + 1
        return id


def salvarProduto(estoque):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)


#exibir menu
while True:
    limpar_tela()
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Entrada de estoque")
    print("4 - Saída de estoque")
    print("5 - Remover produto")
    print("0 - Sair")
    opcao = input(f"\nescolha uma opcao: ")

    if opcao == '1':
        #funcao limpar tela
        limpar_tela()
        #cadastro
        estoque = carregarEstoque() #pega lista
        novoID = gerarId(estoque)#manda lista pro gerar, que pega a qnt de elementos,soma 1 e retorna

        produto = {
            "id": novoID,
            "nome": input("Digite o nome do produto: "),
            "quantidade": int(input("Digite a quantidade do produto: ")),
            "preco": float(input("Digite o preço do produto: "))
        }

        estoque.append(produto)
        salvarProduto(estoque)

        try:
            input("Aperte 'enter' para finalizar... ")
        except KeyboardInterrupt:
            print("Finalizando a operação...")

    elif opcao == '2':
        #funcao limpar
        limpar_tela()
        #exibir produtos do estoque
        estoque = carregarEstoque()
        for produto in estoque:
            print(f"ID: {produto['id']}| Produto: {produto['nome']} | Quantidade: {produto['quantidade']} | Preço: {produto['preco']:.2f}")

        try:
            input("Aperte 'enter' para finalizar... ")
        except KeyboardInterrupt:
            print("Finalizando a operação...")

    elif opcao == '3':
        #funcao limpar
        limpar_tela()
        estoque = carregarEstoque()
        #receber quantidade de produto que chegou e somar
        idEscolhido = input("Digite o id do produto: ")
        encontrado = False

        for produto in estoque:
            if produto["id"] == int(idEscolhido):
                quantidadeSomada = int(input("Digite a quantidade recebida do produto: "))
                produto["quantidade"] += quantidadeSomada
                encontrado = True
                break

        if encontrado == False:
            print("\nProduto não encontrado :/\n")

        salvarProduto(estoque)
        # verificar se é número
        try:
            input("Aperte 'enter' para finalizar... ")
        except KeyboardInterrupt:
            print("Finalizando a operação...")

    elif opcao == '4':
        #funcao limpar
        limpar_tela()
        estoque = carregarEstoque()
        # receber quantidade de produto que chegou e somar
        idEscolhido = input("Digite o id do produto: ")
        encontrado = False

        for produto in estoque:
            if produto["id"] == int(idEscolhido):
                quantidadeSomada = int(input("Digite a quantidade de saída do produto: "))
                produto["quantidade"] -= quantidadeSomada
                encontrado = True
                break

        if encontrado == False:
            print("\nProduto não encontrado :/\n")

        salvarProduto(estoque)

        try:
            input("Aperte 'enter' para finalizar... ")
        except KeyboardInterrupt:
            print("Finalizando a operação...")
    elif opcao == '5':
        #funcao limpar
        limpar_tela()
        estoque = carregarEstoque()
        #receber o id do produto a remover
        #apagar aquele produto da lista
        idEscolhido = input("Digite o id do produto que deseja remover: ")
        encontrado = False

        #remove é por valor, ai caberia fazer com idEscolhido sem indice
        for indice, produto in enumerate(estoque): #pop remove pela posição, não por identificações
            if produto["id"] == int(idEscolhido):
                estoque.pop(indice)
                encontrado = True
                break

        #verificar se esse id existe
        if encontrado == True:
            salvarProduto(estoque)
        else:
            print("Produto não encontrado :/\n")

        try:
            input("Aperte 'enter' para finalizar... ")
        except KeyboardInterrupt:
            print("Finalizando a operação...")

    elif opcao == '0':
        #funcao limpar
        limpar_tela()
        #sair
        input("Finalizando...").strip()
        break
    else:
        input("A opção que você escolheu não existe! Aperte 'enter' e tente novamente.")
#limpar menu

#verificar qual a opção selecionada

#chamar functions ou fazer entrada e saída de dados aqui


