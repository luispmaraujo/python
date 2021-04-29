print("Qual termo deseja encontrar na sequência de Fibonacci?")
numero = int(input("Digite aqui: "))
ultimoNumero = 1
penultimoNumero = 1

if numero == 1 or numero == 2:
    print("1")

else:
    contador = 3

while contador <= numero:
    numeroAtual = penultimoNumero + ultimoNumero
    penultimoNumero = ultimoNumero
    ultimoNumero = numeroAtual

    contador += 1

print("O número desejado é:", numeroAtual)
