numero_inteiro = input('Digite um numero inteiro:')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)
#modulo de numero inteiro 
    if numero_inteiro % 2 == 0: 
        print(f"{numero_inteiro} é par")
    else:
        print(f"{numero_inteiro} é ímpar")
    
else:
    print('Isso nao é um numero inteiro.')