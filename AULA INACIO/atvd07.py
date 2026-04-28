# 1. Par ou ímpar
def is_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


# 2. Saudação
def saudacao(nome, mensagem="Bom dia"):
    return mensagem + ", " + nome


# 3. Contar letras
def contar_letras(texto):
    contagem = {}
    for letra in texto:
        if letra.isalpha():
            letra = letra.lower()
            if letra in contagem:
                contagem[letra] = contagem[letra] + 1
            else:
                contagem[letra] = 1
    return contagem


# 4. Soma de vários números
def soma_tudo(*numeros):
    soma = 0
    for n in numeros:
        soma = soma + n
    return soma


# 5. Maior e menor
def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]

    for n in lista:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    return maior, menor


# ===== Programa =====

# 1
numero = int(input("Digite um número: "))
print("Resultado:", is_par(numero))

# 2
nome = input("Digite seu nome: ")
print(saudacao(nome))

mensagem = input("Digite outra saudação: ")
print(saudacao(nome, mensagem))

# 3
texto = input("Digite um texto: ")
print("Contagem:", contar_letras(texto))

# 4
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
print("Soma:", soma_tudo(n1, n2, n3))

# 5
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

maior, menor = maior_menor([a, b, c])
print("Maior:", maior)
print("Menor:", menor)