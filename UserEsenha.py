usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_dba = 'dani'
senha_dba = '123456'

if usuario_dba == usuario and senha_dba == senha:
    print('Voce está logado no sistema')
else: 
    print('usuário ou senha inválidos.')