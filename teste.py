email = 'rodrigo@gmail.com'

with open('usuarios.txt','r', encoding='utf-8') as arquivo:
    usuarios = []
    for linha in arquivo:
        usuarios.append(linha.strip())
        

# if usuarios[usuarios.index(email)] == 'rodrigo@gmail.com':
#     print('Usuario existente')
# else:
#     print('Usuario inexistente')