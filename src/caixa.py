from banco import ler_estoque_db
from crud import abrir_caixa
from menu import digitar_opcao_inicial,digitar_opcao_2


estoque_infos = ler_estoque_db() #A informaçao do estoque com produtos
menu_estoque = digitar_opcao_2
#Caixa com as operaçoes
opcao = digitar_opcao_inicial()
while (True):
    match (opcao):
        case 0: 
            print("Fechando o caixa")
            break
        case 1: 
            abrir_caixa(estoque_infos)
            menu_estoque()
        case _: 
            print("Error! Opçao invalida")
    opcao = digitar_opcao_inicial()
    



    

   

