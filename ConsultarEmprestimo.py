# Operadores Relacionais
# == igual > maior que
# >= maior ou igual que 
# < menor que <= menor ou igual 
# != diferente

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)


#Limite para pegar emprestimo 
idade_minima = 18
idade_maxima = 30


if idade >= idade_minima and idade <= idade_maxima:
    print(f'{nome} emprestimo aprovado.')
else:
    print(f'{nome} emprestimo negado.')
