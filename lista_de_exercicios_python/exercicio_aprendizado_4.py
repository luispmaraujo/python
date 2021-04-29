import math

a = int(input("Insira o valor de A: "))
print("O valor de A é: ", a)

b = int(input("Insira o valor de B: "))
print("O valor de B é: ", b)

c = int(input("Insira o valor de C: "))
print("O valor de C é: ", c)

delta = math.pow(b, 2) - ((4 * a) * c)
print("O valor de Delta é: ", delta)

raiz1 = (-b + math.sqrt(delta)) / (2 * a)
print("O valor da primeira raiz é: ", raiz1)

raiz2 = (-b - math.sqrt(delta)) / (2 * a)
print("O valor da primeira raiz é: ", raiz2)
