a = int(input("informe o valor: "))
b = int(input("informe o valor: "))
c = int(input("informe o valor: "))
d = int(input("informe o valor: "))

somacd = c + b
if b > c and d > a and (c+d) > (a+b) and c > 0 and b > 0 and a%2==0:

    print("\nValores aceito")
else: 
    print("\nValores não aceitos")