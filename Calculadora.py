calculo = input ('Qual operaodor desejado (soma, sub, multi, divi):')

n1 = input('digite o n1:')
n2 = input('digite o n2:')

if calculo == 'soma':
    saida = int(n1) + int(n2)
if calculo == 'sub':
    saida = int(n1) - int(n2)
if calculo == 'multi':
    saida == int(n1) * int(n2)
if calculo == 'divi':
    saida = int(n1) / int(n2)
else: 
    saida = "Erro"

print('Resultado final:' + str(saida))