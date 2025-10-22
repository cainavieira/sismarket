from banco import ler_estoque_db

estoque_infos = ler_estoque_db()

# Procurar conta especifica
def pesquisar_produto(estoque_infos, id):
    produto_procurado = None
    for info in estoque_infos:
        if (info[0] == id):
            produto_procurado = info
            break
        
    return produto_procurado
      
#Valida que seja numero
def validar_inteiro(msg): 
    while (True):
        try:
            num = int(input(msg))
            break
        except ValueError :
            print("Erro! Input deve ser um numero")
    return num
        
#Valida um numero maior que zero (erro logico)
def entrar_inteiro(msg): 
    while (True):
        num = validar_inteiro(msg)
        if (num > 0):
                break
        else:
            print("Erro! Numero precisa ser maior que zero.")
    return num

def validar_float(msg):
    while (True):
        try:
            num = float(input(msg))
            break
        except ValueError :
            print("Erro! Input deve ser deve ser um numero")
    return num

def entrar_float(msg): 
    while (True):
        num = validar_float(msg)
        if (num > 0):
                break
        else:
            print("Erro! Numero precisa ser maior que zero.")
    return num

# def check_produto():
    