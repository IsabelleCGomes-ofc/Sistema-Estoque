from utils import limpar_tela
from data import  carregarEstoque, gerarId, salvarProduto

def cadastrarProduto():
    limpar_tela()

    estoque = carregarEstoque()
    novoID = gerarId(estoque)

    produto = {
            "id": novoID,
            "nome": input("Digite o nome do produto: "),
            "quantidade": int(input("Digite a quantidade do produto: ")),
            "preco": float(input("Digite o preço do produto: "))
    }

    estoque.append(produto)
    salvarProduto(estoque)
