# Pedir o número ao usuário
N = int(input("Digite um número: "))

# Calcular a soma
soma = 0
for i in range(1, N + 1):
    soma += i

# Mostrar o resultado
print("A soma de 1 até", N, "é:", soma)