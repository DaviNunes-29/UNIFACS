#tendo como dados de entrada 
#a altura 
#o sexo de uma pessoa
#contrua um algoritimo que
#calcule seu peso ideal,
#ultilizando as seguintes formulas
#questao 13

sexo = input("indforme seu sexo - masculino ou feminino: ")
altura = float(input("informe sua altura em metros"))
 
if(sexo == "masculino" or "Masculino" or "M" or "m"):
    pesoIdeal = (72.7 * altura)-58
else:
    pesoIdeal = (62.1 * altura) - 44.7

    
print ("seu peso ideal é: ", pesoIdeal)