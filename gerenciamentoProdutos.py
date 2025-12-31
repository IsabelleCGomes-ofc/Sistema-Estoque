from utils import limpar_tela
from data import  *
from validacoes import *

#----------------------cadastrar------------------------------------------------------------------
def cadastrarProduto():
    limpar_tela()

    estoque = carregarEstoque()
    novoID = gerarId(estoque)
    nome = validarTexto()
    quantidade = validarInteiro()
    preco = validarReal()

    produto = {
            "id": novoID,
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
    }

    estoque.append(produto)
    salvarProduto(estoque)
#--------------------listar-------------------------------------------------------------------------
def listarProdutos():
    limpar_tela()
    # exibir produtos do estoque
    estoque = carregarEstoque()
    if len(estoque) == 0 :
        print("Não há produtos na lista!")

    for produto in estoque:
        print(
            f"ID: {produto['id']}| Produto: {produto['nome']} | Quantidade: {produto['quantidade']} | Preço: {produto['preco']:.2f}")


#-----------------------Movimentar------------------------------------------------------------------
def movimentarQuantidade(opcao):

    limpar_tela()
    estoque = carregarEstoque()
    # receber quantidade de produto que chegou e somar
    idEscolhido = validarID()
    encontrado = False

    for produto in estoque:
        if produto["id"] == idEscolhido:
            while True:
                qtdNova = validarInteiro()

                if opcao == "3":
                    produto["quantidade"] += qtdNova
                    break
                elif opcao == "4":
                    if qtdNova > produto["quantidade"]:
                        print(
                            "A quantidade retirada deve ser menor à quantidade estocada."
                        )
                        continue  # repete a DIGITAÇÃO da quantidade
                    else:
                        produto["quantidade"] -= qtdNova
                        break

            encontrado = True
            break

    encontrarProduto(encontrado, estoque)
    if encontrado:
        salvarProduto(estoque)

#------------------remover---------------------------------------------------------------------
def removerProduto():
    limpar_tela()
    estoque = carregarEstoque()
    # receber o id do produto a remover
    # apagar aquele produto da lista
    idEscolhido = validarID()
    encontrado = False

    # remove é por valor, ai caberia fazer com idEscolhido sem indice
    for indice, produto in enumerate(estoque):  # pop remove pela posição, não por identificações
        if produto["id"] == idEscolhido:
            estoque.pop(indice)
            encontrado = True
            break
    # verificar se esse id existe
    encontrarProduto(encontrado, estoque)