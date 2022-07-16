#Exercício 01
hora = int(input("Digite uma hora"))

if(hora >= 0 and hora <= 5):
    print("Boa madrugada!")
elif(hora >= 6 and hora <= 11):
    print("Bom dia!")
elif(hora >= 12 and hora <= 17):
    print("Boa tarde!")
elif(hora >= 18 and hora <= 23):
    print("Boa noite!")

#Exercício 02
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 9:
    print(f"A média do aluno é {media}")
    print("Aprovado com louvor")
elif media >= 7 and media < 9:
    print(f"A média do aluno é {media}")
    print("Aprovado")
elif media >= 4 and media < 7:
    print(f"A média do aluno é {media}")
    print("Recuperação")
else:
    print(f"A média do aluno é {media}")
    print("Reprovado direto")

#Exercício 3
altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))

imc = (peso / (altura * altura))

if imc < 18.5:
    print("Magreza")
elif 18.5 <= imc <= 24.9:
    print("Normal")
elif 25.0 <= imc <= 29.9:
    print("Sobrepeso")
elif 30.0 <= imc < 39.9:
    print("Obesidade")
else:
    print("Obesidade grave")

#Exercício 4
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if(lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
    print("Equilátero")
elif(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
    print("Escaleno")
else:
    print("Isósceles")

#Exercício 5
dia = int(input("Digite o número correspondente ao dia semana. Exemplo: Segunda = 2, Sábado 7, etc: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Digitou um número diferente de 1 a 7")

#Exercício 6
pergunta1 = input("Telefonou para a vítima: Sim ou Não: ")
pergunta2 = input("Esteve no local do crime: Sim ou Não: ")
pergunta3 = input("Mora perto da vítima: Sim ou Não: ")
pergunta4 = input("Devia para a vítima: Sim ou Não: ")
pergunta5 = input("Já trabalhou com a vítima: Sim ou Não: ")

perguntasPositivas = 0
perguntasNegativas = 0

if pergunta1 == 'Sim':
    perguntasPositivas += 1
else:
    perguntasNegativas += 1

if pergunta2 == 'Sim':
    perguntasPositivas += 1
else:
    perguntasNegativas += 1

if pergunta3 == 'Sim':
    perguntasPositivas += 1
else:
    perguntasNegativas += 1

if pergunta4 == 'Sim':
    perguntasPositivas += 1
else:
    perguntasNegativas += 1

if pergunta5 == 'Sim':
    perguntasPositivas += 1
else:
    perguntasNegativas += 1

if perguntasPositivas == 0:
    print("Ignorar pois não tem envolvimento com o caso")
elif perguntasPositivas <= 2:
    print("Suspeito")
elif perguntasPositivas <= 4:
    print("Cúmplices")
else:
    print("Assassino")

print(f"O número de respostas positivas é {perguntasPositivas}")
print(f"O número de respostas negativas é {perguntasNegativas}")