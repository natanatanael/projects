from time import sleep
from django.db.models.fields import BooleanField
from django.db.models.indexes import Index
import requests
import json
from django.db import models


bases = requests.get("http://127.0.0.1:8000/bases/")
bases = bases.json()

agendamentos = requests.get("http://127.0.0.1:8000/agendamentos/")
agendamentos = agendamentos.json()


# Função separa linhas
def separa():
   print("="*40)

# Requisições HTTP relacionadas às Bases
def visualizar_bases():
    for c, base in enumerate(bases):
        for k, v in bases[c].items():
            print(f"{k} = {v}")
        separa()
def cadastrar_base():
    url_cadastro = "http://127.0.0.1:8000/bases/"
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
    print(f'A base {cadastro_data["nome_base"]} foi cadastrada com sucesso!')
    separa()
def editar_base():
    id_base = int(input("Digite o ID da base que gostaria de alterar: "))
    lista_id_base = list()
    for c, base in enumerate(bases):
        lista_id_base.append(bases[c]["id_base"])  
        if id_base in lista_id_base:
            index = lista_id_base.index(id_base)
            for k, v in bases[index].items():
                print(f"{k} = {v}")
            separa()
            break
    separa()
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
    print(f'A base {edicao_data["nome_base"]} foi editada com sucesso!')
    separa()
def deletar_base():
    id_base = int(input("Digite o ID da base que gostaria de excluir: "))
    lista_id_base = list()
    for c, base in enumerate(bases):
        lista_id_base.append(bases[c]["id_base"])  
        if id_base in lista_id_base:
            index = lista_id_base.index(id_base)
            for k, v in bases[index].items():
                print(bases[index])
                separa()
                break
        else:
            pass
            """print(f"O ID {id_base} não está cadastrado. Tente novamente")
            separa()
            break"""
    url_delete_base = f"http://127.0.0.1:8000/bases/{id_base}/"
    confirma = str(input(f"Tem certeza que deseja excluir a base {id_base}? [S/N] ")).strip().upper()
    if confirma == "S":
        deletar_base = requests.delete(url=url_delete_base)
        print(f"A base {id_base} foi excluída com sucesso!")
        separa()
    else:
        print(f"A base {id_base} não foi exluída.")
        separa()

# Requisições HTTP relacionadas aos Agendamentos
def visualizar_agendamentos():
    for c, agendamento in enumerate(agendamentos):
        for k, v in agendamentos[c].items():
            print(f"{k} = {v}")
        separa()
def novo_agendamento():
    url_agenda = "http://127.0.0.1:8000/agendamentos/"
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
    print(f'O agendamento para a base {agenda_data["id_base"]} foi realizado com sucesso!')
    separa()
def editar_agendamento():
    id_agenda = int(input("Digite o ID do agendamento que gostaria de alterar: "))
    id_list = list()
    for c, agendamento in enumerate(agendamentos):
        id_list.append(agendamentos[c]["id_agendamento"])  
        if id_agenda in id_list:
            index = id_list.index(id_agenda)
            for k, v in agendamentos[index].items():
                print(f"{k} = {v}")
            separa()
            break
    separa()    
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
def deletar_agendamento():
    id_agenda = int(input("Digite o ID do agendamento que gostaria de excluir: "))
    lista_id_agenda = list()
    for c, agendamento in enumerate(agendamentos):
        lista_id_agenda.append(agendamentos[c]["id_agendamento"])  
        if id_agenda in lista_id_agenda:
            index = lista_id_agenda.index(id_agenda)
            for k, v in agendamentos[index].items():
                print(agendamentos[index])
                separa()
                break
            break    
        """else:
            print(f"O ID {id_agenda} não está cadastrado. Tente novamente")"""
    url_delete_agenda = f"http://127.0.0.1:8000/agendamentos/{id_agenda}/"
    confirma = str(input(f"Tem certeza que deseja excluir o agendamento {id_agenda}? [S/N] ")).strip().upper()[0]
    if confirma == "S":
        deletar_agendamento = requests.delete(url=url_delete_agenda)
        print(f"O agendamento {id_agenda} foi excluído com sucesso!")
        separa()
    else:
        print(f"O agendamento {id_agenda} não foi excluído")
        separa()        


opcao = 0
while opcao != 5:
    def menu_inicial():
        separa()
        print("Olá, escolha uma opção abaixo")
        separa()
        print("     [ 1 ] CADASTRAR UMA NOVA BASE")
        print("     [ 2 ] VER A LISTA DE BASES")
        print("     [ 3 ] FAZER UM NOVO AGENDAMENTO")
        print("     [ 4 ] VER TODOS OS AGENDAMENTOS")
        print("     [ 5 ] SAIR DO PROGRAMA")
        separa()
    menu_inicial()
    opcao = int(input("Qual é a sua opção? "))
    if opcao == 1:   # Cadastrar nova base (POST)
        cadastrar_base()
    elif opcao == 2:   # Ver todas as bases (GET)
        visualizar_bases()
        opcao = 0
        while opcao != 4: 
            print("Escolha o que gostaria de fazer agora")
            separa()
            print("     [ 1 ] EDITAR UMA BASE")
            print("     [ 2 ] DELETAR UMA BASE")
            print("     [ 3 ] VOLTAR AO MENU INICIAL")
            print("     [ 4 ] SAIR DO PROGRAMA")
            opcao = int(input("Qual é a sua opção? "))
            print("="*30)
            if opcao == 1: # Editar uma base (PUT)
                editar_base()
            elif opcao == 2: # Deletar uma base (DELETE)
                deletar_base()
            elif opcao == 3:   # Voltar ao Menu
                break
            elif opcao == 4:  # Sair do programa
                print("Finalizando...")
                sleep(2)
                print("Fim do programa")
                exit()
            else:
                print("Opção inválida. Tente novamente.")
    elif opcao == 3:  # Fazer novo agendamento (POST)
        novo_agendamento()
    elif opcao == 4:  # Ver todos os agendamentos (GET)
        visualizar_agendamentos()
        opcao = 0
        while opcao != 4: 
            print("O que você gostaria de fazer agora?")
            separa()
            print("     [ 1 ] EDITAR UM AGENDAMENTO")
            print("     [ 2 ] EXCLUIR UM AGENDAMENTO")
            print("     [ 3 ] VOLTAR AO MENU")
            print("     [ 4 ] SAIR DO PROGRAMA")
            opcao = int(input("Qual é a sua opção? "))
            if opcao == 1: # Editar um agendamento (PUT)
                editar_agendamento()
            elif opcao == 2: # Deletar um agendamento (DELETE)
                deletar_agendamento()
            elif opcao == 3: # Voltar ao menu inicial
                break
            elif opcao == 4: # Sair do programa
                print("Finalizando...")
                sleep(2)
                print("Fim do programa")
                exit()
            else:
                print("Opção inválida. Tente novamente.")
    elif opcao == 5:  # Sair do programa
        print("Finalizando...")
        sleep(1)
    else:
        print("Opção inválida. Tente novamente.")
print("Fim do programa")