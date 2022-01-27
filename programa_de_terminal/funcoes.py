from urls import *


def separa():
   print("="*40)


def encontra_base_itera():
    id_base = int(input("Digite o ID ou nome da base: "))
    lista_id_base = list()
    for c, base in enumerate(bases):
        lista_id_base.append(bases[c]["id_base"])  
        if id_base in lista_id_base:
            index = lista_id_base.index(id_base)
            for k, v in bases[index].items():
                print(f"{k} = {v}")
            separa()
            break
            

