import os

def limpar_tela():
    try:
        os.system('cls' if os.name == 'nt' else 'clear') #funciona em quase tudo
    except:
        print("\n" * 100) #pra funcionar no pycharm

def pausa():
    try:
        input("Aperte ENTER para voltar...")
    except (KeyboardInterrupt, EOFError):
        print("\nFinalizando a operação...")