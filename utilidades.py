import os

def criar_usuario_e_senha(email, senha, janela):        
    with open('usuarios_e_senhas.txt','a', encoding='utf-8', newline='') as arquivo:
        arquivo.write(email + ',' + senha + os.linesep)
    with open('usuarios.txt','a', encoding='utf-8', newline='') as arquivo:
        arquivo.write(email + os.linesep)
    
    janela['conta_criada'].update('Conta Criada!')
    janela['email'].update('')
    janela['senha_cadastro'].update('')
    

def ler_usuario_e_senha(email, senha, janela):
    with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
        usuarios = []
        for linha in arquivo:
            usuarios.append(linha.strip())

    with open('usuarios_e_senhas.txt', 'r', encoding='utf-8') as arquivo:
        senhas = []
        for linha in arquivo:
            senhas.append(linha.strip())

    lista_senha = []

    for password, usuario in zip(senhas, usuarios):
        lista_senha.append(password.split(usuario+',')[1])

    try:
        if email in usuarios and senha in lista_senha:
            janela['usuario_invalido'].update('Usuario Logado com Sucesso!!!')
        else:
            janela['usuario_invalido'].update('ERRO: usuario ou senha incorretos!!!')
    except ValueError:
        janela['usuario_invalido'].update('ERRO: usuario ou senha incorretos!!!')
    
    # try:
    #     if senha in lista_senha:
    #         janela['usuario_invalido'].update('Usuario Logado com Sucesso!!!')
    # except ValueError:
    #     janela['usuario_invalido'].update('ERRO: usuario ou senha incorretos!!!')
