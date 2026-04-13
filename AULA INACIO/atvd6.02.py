dados = {
    "Nome": input("Digite seu nome: "),
    "Idade": int(input("Digite sua idade: ")),
    "Curso": input("Digite seu curso: ")
}

# Atualizar o curso
novo_curso = input("Digite o novo curso: ")
dados["Curso"] = novo_curso

print("Dicionário final:", dados)