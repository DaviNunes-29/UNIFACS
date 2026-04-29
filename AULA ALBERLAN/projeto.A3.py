opcao = 0 
def menu():
    while(True):
        print("escolha uma das opções abaixo")
        print("1 - INCLUIR")
        print("2 - ALTERAR")
        print("3 - REMOVER")
        print("4 - LISTAR")
        print("5 - SAIR")
        opcao = int(input())
        if (opcao > 0 and opcao < 5):
            return opcao
        else:
            if (opcao == 5):
                exit(0) #FUNÇÃO PARA SAIR DO SISTEMA


def incluir():
    while True:
        print("--- INCLUIR (COPA) ---")
        print("1 - Incluir seleção")
        print("2 - Incluir jogador")
        print("3 - Incluir estádio")
        print("4 - Voltar")

        opcao = int(input("Escolha: "))

        if opcao == 1:
            print("Seleção incluída!")
        elif opcao == 2:
            print("Jogador incluído!")
        elif opcao == 3:
            print("Estádio incluído!")
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")




while True:
    escolha = menu()

    if escolha == 1:
        incluir()
    elif escolha == 2:
        print("Alterar (não implementado)")
    elif escolha == 3:
        print("Remover (não implementado)")
    elif escolha == 4:
        print("Listar (não implementado)")


























# FAZENDO TRATAMENTO DE EXCESSÃO
try:
    opcao = menu()

except ValueError:
    print("Você digitou  um caracter errado")

except ZeroDivisionError:
    print("Você digitou  um caracter errado")

else: 
    print("codigo executado sem erros")

finally:
    print("fim do programa")










