'''
9. Sistema de Login:
• Peça o nome de usuário e a senha.
• Verifique se o nome de usuário e a senha são válidos.
• Se forem válidos, exiba a mensagem "Login efetuado com sucesso".
• Se não forem válidos, exiba a mensagem "Login inválido".
'''
# Informações de usuário válidas
nome_usuario = 'Maria'
senha_usuario = '1312'

# Solicita nome de usuário e senha
nome = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')

# Verifica se o nome de usuário e a senha são válidos
if nome_usuario == nome and senha_usuario == senha:
    print("Login efetuado com sucesso")
else:
    print("Login inválido")




"""Login = nome + senha
list = Login

for Login in list:
    if nome == [6] and senha == [4]:
     print('Login efetuado com sucesso')
else:
    print('Login inválido')
    """