def validar_numero(texto):
    texto = texto.replace(" ", "").replace("-", "")
    return texto.isdigit()

# Teste
entrada = input("Digite algo: ")
if validar_numero(entrada):
    print("A string contém apenas números.")
else:
    print("A string NÃO contém apenas números.")