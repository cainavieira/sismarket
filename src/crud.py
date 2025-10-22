import tabulate
from util import entrar_float,entrar_inteiro,pesquisar_produto
from datetime import datetime

def entrar_oper():
    while True:
        oper = input("Entre com [V]enda ou [C]ompra: ").upper()
        if(oper not in ["V", "C"]):
            print("Error!\nINVALID OPERATION")
        else:
            break
    return oper

def realizar_oper(qtd,oper,produto):
    if (oper == "C"):
        produto[2]+= qtd
    elif (oper == "V"):
        produto[2]-= qtd
    return oper
    
def abrir_caixa(estoque_infos):
    tabela = [["id","nome","quantidade","preco"]]
    for campo in estoque_infos:
        tabela.append(campo)
    print(tabulate.tabulate(tabela, headers= "firstrow", tablefmt= "fancy_grid"))
    
def inserir_produto(estoque_infos):
    id = len(estoque_infos) + 1
    print("O numero do id que vai ser inseirod na lista é: ",id)
    nome = input("Insira o nome do produto: ") #to do min length
    quantidade = entrar_inteiro(msg= f"Insira a quantidade de {nome}: ")
    preco = entrar_float(msg= f"Insira o preco do {nome}: ")
    estoque_infos.append([id,nome,quantidade,preco])
    print(estoque_infos)
    for info in estoque_infos:
        print(info)
    return estoque_infos
    
def atualizar_estoque(estoque_infos):
    id_produto = entrar_inteiro(msg="Entre com o ID do produto: ")
    produto = pesquisar_produto(estoque_infos,id_produto)
    if not produto:
        print("Esse produto nao existe")
        return
    qnt_total = entrar_inteiro(msg= "Entre com a quantidade: ")
    oper = entrar_oper()
    realizar_oper(qnt_total,oper,produto)
    exibir_estoque(estoque_infos)
    
def exibir_estoque(estoque_infos):
    tabela = [["id","nome","quantidade","preco"]]
    for campo in estoque_infos:
        tabela.append(campo)
    print(tabulate.tabulate(tabela, headers= "firstrow", tablefmt= "fancy_grid"))
    
def exibir_produto(estoque_infos):
   id = entrar_inteiro(msg= "Insira o ID do produto desejado: ")
   produto = pesquisar_produto(estoque_infos,id)
   if (produto):
        tabela = [["id","nome","quantidade","preco"]]
        tabela.append(produto)
        print(tabulate.tabulate(tabela, headers= "firstrow", tablefmt= "fancy_grid"))
   else:
       print("Essa conta nao existe")
       
    
def atender_cliente(estoque_infos,tabela_cliente,id, compras_cliente):
    items= []
    nome = f"Cliente {id}"
    id_produto = entrar_inteiro(msg= f"Ola, {nome}\nSelecione o ID do produto: ")
    produto = pesquisar_produto(estoque_infos,id_produto) 
    if not produto:
        print("Esse produto nao existe")
        return None
    
    quantidade = entrar_inteiro(f"Insira a quantidade de {produto[1]} : ")

    if quantidade > produto[2]:
        print(f"Quantidade indisponível em estoque! Apenas {produto[2]} disponiveis")
        return None
    
    realizar_oper(quantidade,"V",produto)
    preco = produto[3]
    total_produto =  (preco * quantidade)
    total_produto = round(total_produto,1)
    
    
    compras_cliente.append(total_produto) #Valor de cada produto comprado * qt
    total_compra = sum(compras_cliente) #Valor total da compra
    
    items.append(id_produto)
    tabela_cliente.append([id,id_produto,quantidade,preco, total_produto]) #registro de compras por cliente e produtos
    
    
    return tabela_cliente, id, total_compra, items

def exibir_cliente(id,tabela_cliente,total_compra,items):
    data_atual = datetime.now()
    no_micros= data_atual.replace(microsecond=0).strftime("%d/%m/%y %H:%M")
    print(f"\nCliente {id}")
    print(f"{no_micros}\n")
    tabela = [["Item","Produto","Quantidade","Preco", "Total"]]
    for campo in tabela_cliente:
        tabela.append(campo)
    print(tabulate.tabulate(tabela, headers= "firstrow", tablefmt= "simple"))
    print(f"\nItems: {len(items)}\nTotal Compra: {total_compra}\n")
    
def listar_atendimentos(cliente,total,tabela):
    tabela.append([f"Cliente {cliente}", total])
    return tabela
    
def exibir_caixa_fechado(infos,total_cliente):
    print("\nFechamento do Caixa")
    data_atual = datetime.now().replace(microsecond=0).strftime("%d/%m/%y %H:%M")
    print(f"Data: {data_atual}\n")
    
    tabela = [["Cliente", "total"]]
    for campo in infos:
        tabela.append(campo)
    print(tabulate.tabulate(tabela, headers= "firstrow", tablefmt= "simple"))
        
    print(f"\nTotal de Vendas: {total_cliente}\n")
   
def voltar_menu():
     opcao = input("[0]-Sair: ").upper()
     while (opcao != "0"):
        print("Insira o digito correto")
        opcao = input("[0]-Sair: ").upper()

def checar_produtos_sem_estoque(infos):
    tabela_produtos = []
    for info in infos:
        if info[2] == 0:
            tabela_produtos.append([info[1]])
    return tabela_produtos

def exibir_produtos_sem_estoque(infos):
    tabela = [["Produtos sem estoque"]]
    for campo in infos:
        tabela.append(campo)
    print(tabulate.tabulate(tabela, headers= "firstrow", tablefmt= "simple"))
    print("\n")

