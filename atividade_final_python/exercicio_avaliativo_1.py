idade = 18
estadoCivil = ""
solteiras = 0
casadas = 0
divorciadas = 0
viuvas = 0

while idade >= 18:

    print("Qual a idade da pessoa?")
    idade = int(input("Informe aqui: "))

    print("Qual o estado civil da pessoa?")
    estadoCivil = (input("Informe aqui: "))

    if estadoCivil == "solteiro" or estadoCivil == "Solteiro" or estadoCivil == "SOLTEIRO" or estadoCivil == "solteira" or estadoCivil == "Solteira" or estadoCivil == "SOLTEIRA":
        solteiras += 1

    elif estadoCivil == "casado" or estadoCivil == "Casado" or estadoCivil == "CASADO" or estadoCivil == "casada" or estadoCivil == "Casada" or estadoCivil == "CASADA":
        casadas += 1

    elif estadoCivil == "divorciado" or estadoCivil == "Divorciado" or estadoCivil == "DIVORCIADO" or estadoCivil == "casada" or estadoCivil == "Casada" or estadoCivil == "CASADA":
        divorciadas += 1

    elif estadoCivil == "viuvo" or estadoCivil == "Viuvo" or estadoCivil == "VIUVO" or estadoCivil == "viuva" or estadoCivil == "Viuva" or estadoCivil == "VIUVA":
        viuvas += 1

    else:
        print("A informação inserida é incompatível!")
        print("Programa finalizado!")

        print()

        print("A quantidade de solteiros é:", solteiras)
        print("A quantidade de casados é:", casadas)
        print("A quantidade de divorciados é:", divorciadas)
        print("A quantidade de viuvos é:", viuvas)
