from banco import gravar_estoque_db, ler_estoque_db
from crud import inserir_produto,exibir_estoque,atender_cliente,exibir_cliente,listar_atendimentos,exibir_caixa_fechado,exibir_produto,voltar_menu,atualizar_estoque,checar_produtos_sem_estoque,exibir_produtos_sem_estoque
from util import validar_inteiro

#Visualizaçao do menu do caixa

def exibir_menu_Inicial():
    print("[1]- Abrir o caixa")
    print("[0]- Sair")
    
def exibir_menu_estoque():
    print("[0]- Fechar o Caixa")
    print("[1]- Inserir um produto ao estoque")
    print("[2]- Exibir estoque")
    print("[3]- Iniciar Atendimento")
    print("[4]- Atualizar o Estoque")
    print("[5]- Exibir o Produto")

def exibir_menu_atendimento():
     print("[0]- Finalizar o Atendimento")
     print("[1]- Continuar a Comprar")


#Funçoes do caixa
#Para abrir o caixa
def digitar_opcao_inicial():
    OPCOES = (1,2,3,4,5)
    while True:
        exibir_menu_Inicial()
        opcao = validar_inteiro(msg= "Entre com uma opçao: ")
        if (opcao not in OPCOES) and (opcao != 0):
            print("Error! Opçao invalida")
        else:
            break
    return opcao


#Funçoes do  caixa
def digitar_opcao_2():
    estoque_infos = ler_estoque_db()
    id_cliente = 1 
    tabela_clientes = []
    tabela_cliente = []
    total_clientes = 0
    produtos_sem_estoque = [] 
    while (True):
        exibir_menu_estoque()
        compras = []
        opcao = int(input("Entre com uma opçao: "))
        if (opcao == 0):
            exibir_caixa_fechado(tabela_clientes,total_clientes)
            exibir_produtos_sem_estoque(produtos_sem_estoque)
            break
        elif (opcao == 1): 
            novo_estoque = inserir_produto(estoque_infos)
            gravar_estoque_db(novo_estoque)
        elif (opcao == 2):
            exibir_estoque(estoque_infos)
        elif (opcao == 3):
            while (True):
                resultado = atender_cliente(estoque_infos, tabela_cliente, id_cliente, compras)
                if resultado: 
                    tabela_cliente, id_cliente, total_compra, items = resultado
                    gravar_estoque_db(estoque_infos)
                    exibir_cliente(id_cliente, tabela_cliente, total_compra,items)
                    exibir_menu_atendimento()
                    opcao = int(input("Entre com uma opcao: "))
                    if (opcao == 1): continue
                    elif (opcao == 0): 
                        tabela_cliente.clear()
                        listar_atendimentos(id_cliente,total_compra,tabela_clientes)
                        produtos_sem_estoque = checar_produtos_sem_estoque(estoque_infos)
                        total_clientes += total_compra
                        id_cliente+=1
                        break
                    else:
                        print("Numero Invalido\nNumero precisa ser 0 ou 1")
                        while (opcao not in [1,2]):
                            opcao = int(input("Entre com uma opcao: "))
                            print("Numero Invalido\nNumero precisa ser 0 ou 1")
        elif (opcao == 4):
            atualizar_estoque(estoque_infos)
        elif (opcao == 5):
            exibir_produto(estoque_infos) 
            voltar_menu()
        else:
            print("Opçao Invalida")
        