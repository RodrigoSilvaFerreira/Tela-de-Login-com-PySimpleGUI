def separador():
      return print('=-'*20)

with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
        usuarios = []
        for linha in arquivo:
            usuarios.append(linha.strip())

with open('usuarios_e_senhas.txt', 'r', encoding='utf-8') as arquivo:
        senhas = []
        for linha in arquivo:
            senhas.append(linha.strip())

print(senhas)

for senha,usuario in zip(senhas,usuarios):
      print(senha.split(usuario+',')[1])