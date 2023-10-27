import PySimpleGUI as sg
import os
import utilidades as ut

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
            if values['usuario'] == '' and values['senha'] == '':
                janela['usuario_invalido'].update('Por favor, preencher os campos com email e senha!')
            else: 
                ut.ler_usuario_e_senha(values['usuario'], janela)            
        elif event == 'Criar conta':
            janela_login_.hide()
            janela_cadastro_ = janela_cadastro()
    
    # Eventos da janela de Cadastro
    elif janela == janela_cadastro_:
        if event == 'Criar':
            janela['conta_criada'].update('Conta Criada!')
            ut.banco_de_usuarios(values['email'], values['senha_cadastro'])
            janela['email'].update('')
            janela['senha_cadastro'].update('')
        if event == 'Voltar':
            janela_cadastro_.close()
            janela_login_.un_hide()