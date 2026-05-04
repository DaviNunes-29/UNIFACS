def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def menu():
    while True:
        print("\n--- CALCULADORA ---")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "5":
            break

        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if opcao == "1":
            print("Resultado:", somar(a, b))
        elif opcao == "2":
            print("Resultado:", subtrair(a, b))
        elif opcao == "3":
            print("Resultado:", multiplicar(a, b))
        elif opcao == "4":
            print("Resultado:", dividir(a, b))
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()