# Criar variáveis para nome (str), idade (int),
# altura (float) e peso e (float) de uma pessoa
# Criar variável com o ano atual (int)
# Obter ano de nascimento da pessoas (baseado na idade e no ano atual)
# Obter o IMC da pessoa com 2 casas decimas (peso e na altura da pessoa)
# Exibir um texto com todos os valores na tela usando F-String 9com as chaves)

nome = 'Otavio'
idade = 39
altura = 1.69
peso = 70
ano_atual = 2021
nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e {altura} de altura.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')