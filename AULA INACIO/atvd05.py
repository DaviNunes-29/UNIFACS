ladoA = float(input("Digite o valor do lado A do triângulo:"))
ladoB = float(input("Digite o valor do lado B do triângulo:"))
ladoC = float(input("Digite o valor do lado C do triângulo:"))

if (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB):

    if (ladoA == ladoB) and (ladoB == ladoC):
        tipo="Equilátero"
    elif (ladoA == ladoB) or (ladoA == ladoC) or (ladoB == ladoC):
        tipo = "Isóceles" 
    else:
        tipo = "Escaleno"

    resultado=print("Sim, é possivel forma um triângulo, do tipo ", tipo)
else:
    resultado=print("Não é possivel formar um triângulo!!")