tabuada = int(input("Insira o número da tabuada desejada:"))

contador = 1 

while contador <= 10:
    resultado = contador * tabuada
    print(contador, "x", tabuada, "=", resultado)
    contador += 1
print("fim da tabuada")