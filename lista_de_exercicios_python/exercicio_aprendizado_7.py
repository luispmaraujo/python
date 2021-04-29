medida = input("Insira o tipo de medida: ")
print("A medida selecionada é:", medida)

base = float(input("Insira a medida da base do triângulo: "))
print("A medida da base do triângulo é de:", base, medida)

lado1 = float(input("Insira a medida do primeiro lado do triângulo: "))
print("A medida do primeiro lado do triângulo é de:", lado1, medida)

lado2 = float(input("Insira a medida do segundo lado do triângulo: "))
print("A medida do segundo lado do triângulo é de:", lado2, medida)

if (base == lado1 and lado1 == lado2 and lado2 == base):
    print("Com base nas medidas informadas, a forma geométrica é um triângulo equilátero!")

elif (base != lado1 and base != lado2 and lado1 == lado2):
    print("Com base nas medidas informadas, a forma geométrica é um triângulo isósceles!")

elif (base != lado1 and lado1 != lado2 and lado2 != base):
    print("Com base nas medidas informadas, a forma geométrica é um triângulo escaleno!")

else:
    print("Com base nas medidas informadas, a forma geométrica não se trata de um triângulo!")
