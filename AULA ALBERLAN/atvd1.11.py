n1 = int(input("Informe o primeiro número inteiro:"))
n2 = int(input("Informe o segundo número inteiro:"))
n3 = float(input("Informe o terceiro número real:"))

dobro_metade = (n1 * 2) + (n2 / 2)
soma_triplo = (n1 * 3) + n3
potencia = n3**3

if n1 and n2 == int() and n3 == float():
    print("a. O produto do dobro do primeiro com metade do segundo é:", dobro_metade)
    print("b. a soma do triplo do primeiro com o terceiro.", soma_triplo)
    print("o terceiro elevado ao cubo.", potencia)
else: 
    ("Números inválidos!!")