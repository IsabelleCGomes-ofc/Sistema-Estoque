import json
import os

ARQUIVO = "estoque.json"

#--------------------carregar lista--------------------------------------------------
def carregarEstoque():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w") as arquivo:
            json.dump([], arquivo, indent=4)

    with open(ARQUIVO, "r") as arquivo:
        estoqueLista = json.load(arquivo)

    return estoqueLista

#-------------------Gerar ID novo----------------------------------------------------
def gerarId(estoqueLista):
    if len(estoqueLista) == 0: #len=conta quantos elementos tem a variavel, chars, chaves, elementos de lista..
        idPrimário = 1
        return idPrimário
    else:
        ids = [item["id"] for item in estoqueLista] #obs: item é comando de lista
        id = max(ids) + 1
        return id

#-------------------Salvar no arquivo texto------------------------------------------
def salvarProduto(estoque):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(estoque, arquivo, indent=4)