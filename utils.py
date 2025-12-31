import os

#-----------limpar------------------------------------------------------------------
def limpar_tela():
    try:
        os.system('cls' if os.name == 'nt' else 'clear') #funciona em quase tudo
    except:
        print("\n" * 100) #pra funcionar no pycharm

#-----------pausar-------------------------------------------------------------------
def pausa():
    try:
        input("Aperte ENTER para voltar...")
    except (KeyboardInterrupt, EOFError):
        print("\nFinalizando a operação...")