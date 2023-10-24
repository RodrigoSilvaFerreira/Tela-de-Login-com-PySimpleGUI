import PySimpleGUI as sg
import os

sg.theme('Reddit')


def janela_login():
    layout = [
        [sg.Text('Usuário: ')],
        [sg.Input(key='usuario')],
        [sg.Text('Senha: ')],
        [sg.Input(key='senha', password_char='*')],
        [sg.Text(key='usuario_invalido')],
        [sg.Button('Logar')],
        [sg.Text('Não possui uma conta: ')],
        [sg.Button('Criar conta')]
    ]
    return sg.Window('Tela de Login', layout=layout, finalize=True)


def janela_cadastro():
    layout = [
        [sg.Text('Digite seu email: ')],
        [sg.Input(key='email')],
        [sg.Text('Crie sua senha: ', )],
        [sg.Input(key='senha_cadastro', password_char='*')],
        [sg.Text(key='conta_criada')],
        [sg.Button('Criar'), sg.Button('Voltar')]
    ]
    return sg.Window('Janela Cadastro', layout=layout, finalize=True)

janela_login_, janela_cadastro_ = janela_login(), None

while True:
    janela, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break

    # Eventos da janela de Login
    elif janela == janela_login_ :
        if event == 'Logar':
            with open('banco_de_usuarios.txt','r',encoding='utf-8') as arquivo:
                for linha in arquivo:
                    if values['usuario'] != linha:
                        janela['usuario_invalido'].update(text_color='red')
                        janela['usuario_invalido'].update('Usuario/Senha invalido')
                    else:
                        janela['usuario_invalido'].update('Usuario Logado com Sucesso!!!')
                        
        elif event == 'Criar conta':
            janela_login_.hide()
            janela_cadastro_ = janela_cadastro()
    
    # Eventos da janela de Cadastro
    elif janela == janela_cadastro_:
        if event == 'Criar':
            janela['conta_criada'].update('Conta Criada!')
            with open('banco_de_usuarios.txt', 'a', encoding='utf-8', newline='') as arquivo:
                arquivo.write(values['email'] + os.linesep)
                arquivo.write(values['senha_cadastro'] + os.linesep)
            janela['email'].update('')
            janela['senha_cadastro'].update('')
        if event == 'Voltar':
            janela_cadastro_.close()
            janela_login_.un_hide()