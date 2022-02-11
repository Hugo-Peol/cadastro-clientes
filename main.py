import PySimpleGUI as sg
from colorama import Fore


class telaCadastro:
    def __init__(self):
        sg.change_look_and_feel('BlueMono')
        # Layout
        menu_layout = [
            [sg.Text('Cadastrar cliente')],
            [sg.Text('Nome: ', size=(9, 0)), sg.InputText(size=(30, 0), key='nome',)],
            [sg.Text('Telefone: ', size=(9, 0)), sg.InputText(key='telefone')],
            [sg.Text('Endereço: ', size=(9, 0)), sg.InputText(key='endereco')],
            [sg.Button('Cadastrar', key='cadastrar',), sg.Button('Buscar', key='buscar') ,sg.Button('Sair', key='sair')],
            [sg.Output(size=(30, 20))]

        ]
        # Janela

        self.window = sg.Window('Sistema cadastro de clientes', menu_layout, size=(300, 300))



    def Iniciar(self):
        while True:
            # Extrair dados da tela
            self.button, self.values = self.window.Read()
            if self.button == 'cadastrar':
                self.salvarCadastro()
            else:
                print('Erro')

            nome = self.values['nome']
            telefone = self.values['telefone']
            endereco = self.values['endereco']
            print('Cadastrado com sucesso!')
            print(f'Nome: {nome}')
            print(f'Telefone: {telefone}')
            print(f'Endereço: {endereco}')

    def salvarCadastro(self):
        nome = self.values['nome']
        telefone = self.values['telefone']
        endereco = self.values['endereco']
        with open('cadastro.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
            arquivo.writelines(f'Nome :{nome} Telefone:{telefone} Endereço:{endereco}\n')
            print('Cadastrado com sucesso')











tela = telaCadastro()
tela.Iniciar()
