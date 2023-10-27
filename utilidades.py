import os

def banco_de_usuarios(email, senha):        
    with open('usuarios_e_senhas.txt','a', encoding='utf-8', newline='') as arquivo:
        arquivo.write(email + ',' + senha + os.linesep)
    with open('usuarios.txt','a', encoding='utf-8', newline='') as arquivo:
        arquivo.write(email + os.linesep)
    

def ler_usuario_e_senha(email, janela):
    with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
        usuarios = []
        for linha in arquivo:
            usuarios.append(linha.strip())
            
    try:
        if usuarios[usuarios.index(email)] in email:
            janela['usuario_invalido'].update('Usuario Logado com Sucesso!!!')
    except ValueError:
        janela['usuario_invalido'].update('Usuario inexistente!!!')

