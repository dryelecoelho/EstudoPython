num_inteiro = input('Digite um numero inteiro: ')

if num_inteiro.isdigit():
    num_inteiro = int(num_inteiro)

    if num_inteiro % 2 == 0:
        print(f'{num_inteiro} é par')
    else:
        print(f'{num_inteiro} é ímpar')
else:
    print('Isso não é um número inteiro')

