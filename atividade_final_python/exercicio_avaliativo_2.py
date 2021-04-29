# Menu de Opções - Saída de dados

print("Tabuada de Multiplicação")

print("========================")

print()

print("Opção 1 - Tabuada do 1")
print("Opção 2 - Tabuada do 2")
print("Opção 3 - Tabuada do 3")
print("Opção 4 - Tabuada do 4")
print("Opção 5 - Tabuada do 5")
print("Opção 6 - Tabuada do 6")
print("Opção 7 - Tabuada do 7")
print("Opção 8 - Tabuada do 8")
print("Opção 8 - Tabuada do 9")
print("Opção 10 - Tabuada do 10")
print("Opção 11 - Sair do programa")

print()
print("========================")
print()

# Entrada de dados

print("Qual opção deseja escolher?")
opcao = int(input("Digite aqui: "))

# Processamento e saída

if opcao >= 11:
    print("Programa finalizado!")
else:
    for i in range(1, 11, 1):
        print(opcao, "*", i, "=", opcao * i)
