#Importar csv e exportar csv

ARQ = "src/estoque.csv"

def ler_estoque():
    storage = []
    try:
        with open(ARQ,mode= "r",encoding="UTF-8") as arq:
            for row in arq:
                campos = row.split(",")
                id, nome, quantidade, preco = int(campos[0]),campos[1],int(campos[2]),float(campos[3]),
                storage.append([id,nome,quantidade,preco])
    except Exception as error:
        print(error)
    return storage


def gravar_estoque(caixa_infos):
    try:
        with open(ARQ,mode= "w",encoding="UTF-8") as arq:
            for info in caixa_infos:
                arq.write(f"{info[0]},{info[1]},{info[2]},{info[3]}\n")
    except Exception as error:
        print(error)