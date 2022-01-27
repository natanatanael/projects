from time import sleep
from django.db.models.fields import BooleanField
from django.db.models.indexes import Index
import requests



def menu_geral():
    ("     [ 1 ] CADASTRAR UMA NOVA BASE")
    ("     [ 2 ] VER A LISTA DE BASES")
    ("     [ 3 ] FAZER UM NOVO AGENDAMENTO")
    ("     [ 4 ] VER TODOS OS AGENDAMENTOS")
    ("     [ 5 ] SAIR DO PROGRAMA")
    return menu_geral


def menu_edicao():
    print("     [ 1 ] CADASTRAR UMA NOVA BASE")
    print("     [ 2 ] EDITAR UMA BASE")
    print("     [ 3 ] DELETAR UMA BASE")
    print("     [ 4 ] FAZER UM NOVO AGENDAMENTO")
    print("     [ 5 ] VER TODOS OS AGENDAMENTOS")
    print("     [ 6 ] SAIR DO PROGRAMA")
    return menu_edicao


def separa():
   print("="*40)

bases = requests.get("http://127.0.0.1:8000/bases/")
bases = bases.json()

agendamentos = requests.get("http://127.0.0.1:8000/agendamentos/")
agendamentos = agendamentos.json()

# Cadastrar uma nova base (POST)
url_cadastro = "http://127.0.0.1:8000/bases/"

# Fazer agendamento
url_agenda = "http://127.0.0.1:8000/agendamentos/"


#laço para ver todas as bases (GET)
"""for c, base in enumerate(bases):
    for k, v in bases[c].items():
        print(f"{k} = {v}")
    print("="*40)"""


"""for k in bases.keys():
    input()
    print("="*40)"""

     
# laço para ver uma única base (GET)
"""for k, v in bases[0].items():
    print(f"{k} = {v}")""" 



print("Olá, escolha uma opção abaixo")

opcao = 0
while opcao != 5:
    print("     [ 1 ] CADASTRAR UMA NOVA BASE")
    print("     [ 2 ] VER A LISTA DE BASES")
    print("     [ 3 ] FAZER UM NOVO AGENDAMENTO")
    print("     [ 4 ] VER TODOS OS AGENDAMENTOS")
    print("     [ 5 ] SAIR DO PROGRAMA")
    opcao = int(input("Qual é a sua opção? "))
    print("="*30)
    if opcao == 1:   # Cadastrar nova base (POST)
        cadastro_data = {
        "nome_base": "", 
        "status_base": "",
        "prazo_entrega": "",
        "volume_dia": "",
        "faz_coleta": False,
        "cnpj": "",
        "nome_proprietario_base": "",
        "nome_gestor_base": "",
        "telefone": "",
        "endereco": "",
        "numero_endereco": "",
        "bairro_endereco": "",
        "cidade": "",
        "estado": "",
        "cep": "",
        "regional": "",
        "analista_responsavel": ""
        }
        cadastro_data["nome_base"] = str(input("Nome da base: "))
        cadastro_data["status_base"] = str(input("Status da base: "))
        cadastro_data["prazo_entrega"] = str(input("Prazo de entrega(D): "))
        cadastro_data["volume_dia"] = int(input("Volume/dia: "))
        cadastro_data["cnpj"] = int(input("CNPJ: "))
        cadastro_data["nome_proprietario_base"] = str(input("Nome Proprietario da base: "))
        cadastro_data["nome_gestor_base"] = str(input("Nome Gestor da base: "))
        cadastro_data["telefone"] = int(input("Telefone: "))
        cadastro_data["endereco"] = str(input("Endereço: "))
        cadastro_data["numero_endereco"] = int(input("Número do endereco: "))
        cadastro_data["bairro_endereco"] = str(input("Bairro do endereco: "))
        cadastro_data["cidade"] = str(input("Cidade: "))
        cadastro_data["estado"] = str(input("Estado: "))
        cadastro_data["cep"] = int(input("CEP: "))
        cadastro_data["regional"] = int(input("Regional: "))
        cadastro_data["analista_responsavel"] = str(input("Analista responsavel: "))
        cadastrar_base = requests.post(url=url_cadastro, json=cadastro_data)
    elif opcao == 2:   # Ver todas as bases (GET)
        for c, base in enumerate(bases):
            for k, v in bases[c].items():
                print(f"{k} = {v}")
            print("="*40)
            print("Escolha o que gostaria de fazer agora")
            separa()
            opcao = 0
        while opcao != 5: 
            print("     [ 1 ] CADASTRAR UMA NOVA BASE")
            print("     [ 2 ] EDITAR UMA BASE")
            print("     [ 3 ] DELETAR UMA BASE")
            print("     [ 4 ] FAZER UM NOVO AGENDAMENTO")
            print("     [ 5 ] VER TODOS OS AGENDAMENTOS")
            print("     [ 6 ] SAIR DO PROGRAMA")   
            opcao = int(input("Qual é a sua opção? "))
            print("="*30)
            if opcao == 1:   # Cadastrar nova base (POST)
                cadastro_data = {
                "nome_base": "", 
                "status_base": "",
                "prazo_entrega": "",
                "volume_dia": "",
                "faz_coleta": False,
                "cnpj": "",
                "nome_proprietario_base": "",
                "nome_gestor_base": "",
                "telefone": "",
                "endereco": "",
                "numero_endereco": "",
                "bairro_endereco": "",
                "cidade": "",
                "estado": "",
                "cep": "",
                "regional": "",
                "analista_responsavel": ""
                }
                cadastro_data["nome_base"] = str(input("Nome da base: "))
                cadastro_data["status_base"] = str(input("Status da base: "))
                cadastro_data["prazo_entrega"] = str(input("Prazo de entrega(D): "))
                cadastro_data["volume_dia"] = int(input("Volume/dia: "))
                cadastro_data["cnpj"] = int(input("CNPJ: "))
                cadastro_data["nome_proprietario_base"] = str(input("Nome Proprietario da base: "))
                cadastro_data["nome_gestor_base"] = str(input("Nome Gestor da base: "))
                cadastro_data["telefone"] = int(input("Telefone: "))
                cadastro_data["endereco"] = str(input("Endereço: "))
                cadastro_data["numero_endereco"] = int(input("Número do endereco: "))
                cadastro_data["bairro_endereco"] = str(input("Bairro do endereco: "))
                cadastro_data["cidade"] = str(input("Cidade: "))
                cadastro_data["estado"] = str(input("Estado: "))
                cadastro_data["cep"] = int(input("CEP: "))
                cadastro_data["regional"] = int(input("Regional: "))
                cadastro_data["analista_responsavel"] = str(input("Analista responsavel: "))
                cadastrar_base = requests.post(url=url_cadastro, json=cadastro_data)
                menu_geral()
            elif opcao == 2: # Editar uma base (PUT)
                id_base = int(input("Digite o ID da base que gostaria de alterar: "))
                bases = requests.get("http://127.0.0.1:8000/bases/") 
                bases = bases.json()
                for k, v in bases[id_base-1].items():
                    print(f"{k} = {v}")
                print("="*40)
                url_edicao_base = f"http://127.0.0.1:8000/bases/{id_base}/"
                edicao_data = {
                "nome_base": "", 
                "status_base": "",
                "prazo_entrega": "",
                "volume_dia": "",
                "faz_coleta": False,
                "cnpj": "",
                "nome_proprietario_base": "",
                "nome_gestor_base": "",
                "telefone": "",
                "endereco": "",
                "numero_endereco": "",
                "bairro_endereco": "",
                "cidade": "",
                "estado": "",
                "cep": "",
                "regional": "",
                "analista_responsavel": ""
                }
                """campos_edicao = int(input("Digite"))"""
                edicao_data["nome_base"] = input("Nome da base: ")
                edicao_data["status_base"] = input("Status da base: ")
                edicao_data["prazo_entrega"] = input("Prazo de entrega(D): ")
                edicao_data["volume_dia"] = input("Volume/dia: ")
                edicao_data["cnpj"] = input("CNPJ: ")
                edicao_data["nome_proprietario_base"] = input("Nome Proprietario da base: ")
                edicao_data["nome_gestor_base"] = input("Nome Gestor da base: ")
                edicao_data["telefone"] = input("Telefone: ")
                edicao_data["endereco"] = input("Endereço: ")
                edicao_data["numero_endereco"] = input("Número do endereco: ")
                edicao_data["bairro_endereco"] = input("Bairro do endereco: ")
                edicao_data["cidade"] = input("Cidade: ")
                edicao_data["estado"] = input("Estado: ")
                edicao_data["cep"] = input("CEP: ")
                edicao_data["regional"] = input("Regional: ")
                edicao_data["analista_responsavel"] = input("Analista responsavel: ")
                editar_base = requests.put(url=url_edicao_base, json=edicao_data)
                menu_geral()
            elif opcao == 3:
                pass
            
            elif opcao == 4:   # Fazer novo agendamento (POST)
                agenda_data = {
                "data_hora": "",
                "cancelado": False,
                "tipo_agendamento": "",
                "obs": "",
                "id_base": ""
                }
                agenda_data["data_hora"] = str(input("Data_Hora[AAAA-MM-DD 00:00]: "))
                agenda_data["tipo_agendamento"] = str(input("Tipo de agendamento: "))
                agenda_data["obs"] = str(input("Observações: "))
                agenda_data["id_base"] = int(input("ID da base: ")) 
                fazer_agendamento = requests.post(url=url_agenda, json=agenda_data)
                menu_geral()
            elif opcao == 5:  # Ver todos os agendamentos (GET)
                for c, agendamento in enumerate(agendamentos):
                    for k, v in agendamentos[c].items():
                        print(f"{k} = {v}")
                    print("="*30)
                print("O que você gostaria de fazer agora?")
                opcao = 0
                while opcao != 3: 
                    print("     [ 1 ] EDITAR UM AGENDAMENTO")
                    print("     [ 2 ] VOLTAR AO MENU")
                    print("     [ 3 ] SAIR DO PROGRAMA")
                    opcao = int(input("Qual é a sua opção? "))
                    separa
                    if opcao == 1: # Editar um agendamento (PUT)
                        id_agendamento = int(input("Digite o ID do agendamento que gostaria de alterar: "))
                        agendamentos = requests.get("http://127.0.0.1:8000/agendamentos/") 
                        agendamentos = agendamentos.json()
                        for k, v in agendamentos[id_agendamento-1].items():
                            print(f"{k} = {v}")
                        print("="*40)
                        url_edicao_base = f"http://127.0.0.1:8000/bases/{id_agendamento}/"
                    elif opcao == 2:
                        pass
                    else:
                        print("Opção Inválida")
                
            elif opcao == 6:    # Sair do programa
                print("Finalizando...")
                sleep(2)
            else:
                print("Opção inválida. Tente novamente.")
    
    elif opcao == 3:  # Fazer novo agendamento (POST)
        agenda_data = {
        "data_hora": "",
        "cancelado": False,
        "tipo_agendamento": "",
        "obs": "",
        "id_base": ""
        }
        agenda_data["data_hora"] = str(input("Data_Hora[AAAA-MM-DD 00:00]: "))
        agenda_data["tipo_agendamento"] = str(input("Tipo de agendamento: "))
        agenda_data["obs"] = str(input("Observações: "))
        agenda_data["id_base"] = int(input("ID da base: ")) 
        fazer_agendamento = requests.post(url=url_agenda, json=agenda_data)
    
    elif opcao == 4:  # Ver todos os agendamentos (GET)
        for c, agendamento in enumerate(agendamentos):
            for k, v in agendamentos[c].items():
                print(f"{k} = {v}")
            print("="*30)
        print("O que você gostaria de fazer agora?")    
        while opcao != 3: 
            print("     [ 1 ] EDITAR UM AGENDAMENTO")
            print("     [ 2 ] VOLTAR AO MENU")
            print("     [ 3 ] SAIR DO PROGRAMA")
            opcao = int(input("Qual é a sua opção? "))
            separa
            if opcao == 1: # Editar um agendamento (PUT)
                id_agenda = int(input("Digite o ID do agendamento que gostaria de alterar: "))
                url_edicao_agenda = f"http://127.0.0.1:8000/agendamentos/{id_agenda}/"
                edicao_agenda_data = {
                "id_agendamento": "",
                "data_hora": "",
                "data_criacao": "",
                "cancelado": False,
                "tipo_agendamento": "",
                "obs": "",
                "id_base": ""
                }
                edicao_agenda_data["data_hora"] = input("Data_Hora[AAAA-MM-DD 00:00]: ")
                edicao_agenda_data["tipo_agendamento"] = input("Tipo de agendamento: ")
                edicao_agenda_data["obs"] = input("Observações: ")
                editar_agendamento = requests.put(url=url_edicao_agenda, json=edicao_agenda_data)
                separa()
                break       
            elif opcao == 2:
                pass
            else:
                print("Opção Inválida")
    elif opcao == 5:  # Sair do programa
        print("Finalizando...")
        sleep(2)
    else:
        print("Opção inválida. Tente novamente.")
print("Fim do programa")