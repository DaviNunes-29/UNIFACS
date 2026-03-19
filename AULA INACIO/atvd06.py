import math

# Leitura dos coeficientes
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

# Verifica se é realmente uma equação do 2º grau
if a == 0:
    print("Não é uma equação do 2º grau.")
else:
    # Cálculo do delta
    delta = b**2 - 4*a*c
    print(f"Delta (Δ) = {delta}")

    # Verificação das raízes
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Duas raízes reais:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

    elif delta == 0:
        x = -b / (2*a)
        print("Uma raiz real (raiz dupla):")
        print(f"x = {x}")

    else:
        print("Não existem raízes reais.")