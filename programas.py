nota1 = float(input("digite a nota 1: "))

nota2 = float(input("digite a nota 2: "))

media = (nota1 + nota2)/2

if media >= 7:
   print("aluno aprovado")

else:
   print("aluno reprovado")

sexo = str(input("f = femi, m = mascu:"))

if sexo == "f":
    print("é feminino")
else:
    print("é masculino")

num1 = str(input("insira um numero:"))
num2 = str(input("insira um numero:"))
num3 = str(input("insira um numero:"))

print(max(num1,num2,num3))
print(min(num1,num2,num3))