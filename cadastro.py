from utils import limpar_tela
from data import  carregarEstoque, gerarId, salvarProduto
from validacoes import validarInteiro, validarTexto, validarReal

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
    print("Produto cadastrado com sucesso!")
