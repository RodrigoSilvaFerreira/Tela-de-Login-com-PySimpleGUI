import PySimpleGUI as sg
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
            if values['usuario'] == '' or values['senha'] == '':
                janela['usuario_invalido'].update('Por favor, preencher os campos usuário e senha!')
            else: 
                ut.ler_usuario_e_senha(values['usuario'], values['senha'] , janela)            
        elif event == 'Criar conta':
            janela_login_.hide()
            janela_cadastro_ = janela_cadastro()
    
    # Eventos da janela de Cadastro
    elif janela == janela_cadastro_:
        if event == 'Criar':
            if values['email'] == '' or values['senha_cadastro'] == '':
                janela['conta_criada'].update('Por favor, preencher os campos senha e email')
            else:    
                ut.criar_usuario_e_senha(values['email'], values['senha_cadastro'], janela)
        if event == 'Voltar':
            janela_cadastro_.close()
            janela_login_.un_hide()