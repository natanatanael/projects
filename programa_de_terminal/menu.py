from classes import separa

class Menu():
    def __init__(self) -> None:
        def cabecalho():
            separa()
            print("Escolha uma opção abaixo:")
            separa()
        self.cabecalho = cabecalho
        

    def menu_inicial(Menu):
        print("     [ 1 ] CADASTRAR UMA NOVA BASE")
        print("     [ 2 ] VER A LISTA DE BASES")
        print("     [ 3 ] FAZER UM NOVO AGENDAMENTO")
        print("     [ 4 ] VER TODOS OS AGENDAMENTOS")
        print("     [ 5 ] INFORMAÇÕES")
        print("     [ 6 ] SAIR DO PROGRAMA")
        separa()

       
    def menu_base(Menu):
        print("     [ 1 ] EDITAR UMA BASE")
        print("     [ 2 ] DELETAR UMA BASE")
        print("     [ 3 ] VOLTAR AO MENU INICIAL")
        print("     [ 4 ] SAIR DO PROGRAMA")
        separa()

    def menu_agendamento(Menu):
        print("     [ 1 ] EDITAR UM AGENDAMENTO")
        print("     [ 2 ] EXCLUIR UM AGENDAMENTO")
        print("     [ 3 ] VOLTAR AO MENU")
        print("     [ 4 ] SAIR DO PROGRAMA")
        separa()

    def menu_informacoes(Menu):
        print("     [ 1 ] CONTATOS DA BASE")
        print("     [ 2 ] CIDADES ATENDIDAS")
        print("     [ 3 ] BASES PRÓXIMAS")
        print("     [ 4 ] PERFORMANCE E VOLUMETRIA")
        print("     [ 5 ] FINANCEIRO")
        print("     [ 6 ] VOLTAR AO MENU INICIAL")
        print("     [ 7 ] SAIR DO PROGRAMA")
        separa()   
    