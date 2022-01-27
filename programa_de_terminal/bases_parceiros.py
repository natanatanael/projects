from time import sleep
from classes import Base, Agendamento, Informacoes
from menu import Menu
from urls import bases, agendamentos

opcao = 0
while opcao != 6:
    inicio = Menu()
    inicio.menu_inicial()
    opcao = int(input("Qual é a sua opção? "))
    if opcao == 1:   # Cadastrar nova base (POST)
        cad_base = Base()
        cad_base.cadastrar_base()
    elif opcao == 2:   # Ver todas as bases (GET)
        visual_base = Base()
        visual_base.visualizar_bases()
        opcao = 0
        while opcao != 4: 
            base_menu = Menu()
            base_menu.menu_base()
            opcao = int(input("Qual é a sua opção? "))
            print("="*30)
            if opcao == 1: # Editar uma base (PUT)
                edit_base = Base()
                edit_base.editar_base()
            elif opcao == 2: # Deletar uma base (DELETE)
                del_base = Base()
                del_base.deletar_base()
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
        cad_agenda = Agendamento()
        cad_agenda.novo_agendamento()
    elif opcao == 4:  # Ver todos os agendamentos (GET)
        visual_agenda = Agendamento()
        visual_agenda.visualizar_agendamentos()
        opcao = 0
        while opcao != 4: 
            agenda_menu = Menu()
            agenda_menu.menu_agendamento()
            opcao = int(input("Qual é a sua opção? "))
            if opcao == 1: # Editar um agendamento (PUT)
                edit_agenda = Agendamento()
                edit_agenda.editar_agendamento()
            elif opcao == 2: # Deletar um agendamento (DELETE)
                del_agenda = Agendamento()
                del_agenda.deletar_agendamento()
            elif opcao == 3: # Voltar ao menu inicial
                break
            elif opcao == 4: # Sair do programa
                print("Finalizando...")
                sleep(2)
                print("Fim do programa")
                exit()
            else:
                print("Opção inválida. Tente novamente.")
    elif opcao == 5:
        while opcao != 7:
            info_menu = Menu()
            info_menu.menu_informacoes()
            opcao = 0
            opcao = int(input("Qual é a sua opção? "))
            if opcao == 1:
                contatos = Informacoes()
                contatos.contatos_base()
            elif opcao == 2:
                atendidas = Informacoes()
                atendidas.cidades_atendidas()
            elif opcao == 3:
                vizinhas = Informacoes()
                vizinhas.bases_proximas()
            elif opcao == 4:
                perform = Informacoes()
                perform.performance()
            elif opcao == 5:
                financ = Informacoes()
                financ.financeiro()
            elif opcao == 6:
                break
            elif opcao == 7:
                print("Finalizando...")
                sleep(2)
                print("Fim do programa")
                exit()
            else:
                print("Opção inválida. Tente novamente.")
    elif opcao == 6:  # Sair do programa
        print("Finalizando...")
        sleep(1)
    else:
        print("Opção inválida. Tente novamente.")
print("Fim do programa")