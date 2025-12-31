from utils import limpar_tela
from data import  carregarEstoque, salvarProduto

def listarProdutos():
    limpar_tela()
    # exibir produtos do estoque
    estoque = carregarEstoque()
    for produto in estoque:
        print(
            f"ID: {produto['id']}| Produto: {produto['nome']} | Quantidade: {produto['quantidade']} | Preço: {produto['preco']:.2f}")



def movimentarQuantidade(opcao):

    limpar_tela()
    estoque = carregarEstoque()
    # receber quantidade de produto que chegou e somar
    idEscolhido = input("Digite o id do produto: ")
    encontrado = False

    for produto in estoque:
        if produto["id"] == int(idEscolhido):
            qtdNova = int(input("Digite a quantidade de produto movimentao: "))
            if opcao == "3":
                produto["quantidade"] += qtdNova
            elif opcao == "4":
                produto["quantidade"] -= qtdNova
            encontrado = True
            break

    if encontrado == False:
        print("\nProduto não encontrado :/\n")

    salvarProduto(estoque)

def removerProduto():
    limpar_tela()
    estoque = carregarEstoque()
    # receber o id do produto a remover
    # apagar aquele produto da lista
    idEscolhido = input("Digite o id do produto que deseja remover: ")
    encontrado = False

    # remove é por valor, ai caberia fazer com idEscolhido sem indice
    for indice, produto in enumerate(estoque):  # pop remove pela posição, não por identificações
        if produto["id"] == int(idEscolhido):
            estoque.pop(indice)
            encontrado = True
            break

    # verificar se esse id existe
    if encontrado == True:
        salvarProduto(estoque)
    else:
        print("Produto não encontrado :/\n")