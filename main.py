from utils import limpar_tela, pausa
from cadastro import cadastrarProduto
from gerenciamentoProdutos import listarProdutos, movimentarQuantidade, removerProduto

def exibirMenu():
    limpar_tela()
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Entrada de estoque")
    print("4 - Saída de estoque")
    print("5 - Remover produto")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

#exibir menu
while True:
    opcao = exibirMenu()

    if opcao == '1':
        cadastrarProduto()
        pausa()

    elif opcao == '2':
        listarProdutos()
        pausa()

    elif opcao == '3' or opcao == '4':
        #funcao limpar
        movimentarQuantidade(opcao)
        pausa()

    elif opcao == '5':
        #funcao limpar
        removerProduto()
        pausa()

    elif opcao == '0':
        #funcao limpar
        limpar_tela()
        #sair
        input("Finalizando...")
        break
    else:
        input("A opção que você escolheu não existe! tente novamente e escolha um número do menu.")


