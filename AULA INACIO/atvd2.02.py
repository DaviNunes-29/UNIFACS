soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))

    if numero == 0:
        break

    soma += numero
    quantidade += 1

print("Soma dos números:", soma)
print("Quantidade de números digitados:", quantidade)