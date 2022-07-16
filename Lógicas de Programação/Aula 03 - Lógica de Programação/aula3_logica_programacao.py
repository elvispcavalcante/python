# Exercícios slides da aula 03

"""
Lembrando de comentários em bloco
"""

print("Prática 01: \n")

import random

continuacao = True
numero_sorteado = random.randrange(1,10)

while continuacao:
    numero = int(input("Tente acertar o número sorteado. Digite um número de 1 a 10 (Se quiser parar digite 0): "))

    if numero == numero_sorteado:
        print("Você acertou o número. PARABÉNS")
        continuacao = False
    elif numero == 0:
        continuacao = False
    else:
        print("Você errou. Tente novamente")

print("\n")
print("Prática 02: \n")

continuacao = True
somaToneladas = 0.0

valorFixoTonelada = float(input("Digite o valor fixo da tonelada: "))


while continuacao:
    toneladasSaiu = float(input("Digite a quantidade toneladas que saiu: "))
    continuar = input("Deseja continuar? Digite sim ou não: ")
    somaToneladas += toneladasSaiu
    if(continuar == "sim"):
        continue
    else:
        break

totalFaturado = somaToneladas * valorFixoTonelada

print(f"O total faturado das toneladas que saíram foi de R$ {totalFaturado:.2f}")

print("\n")
print("Prática 03: \n")

contador = 1
soma_notas = 0.0
continuacao = True

while continuacao:
    nota = input(f"Digite a nota {contador} do aluno: ")
    if nota.replace(".", "").isnumeric():
        nota = float(nota)
        soma_notas += nota
        continuar = input("Deseja continuar? sim ou não: ")
        if continuar == "sim":
            contador += 1
            continue
        elif continuar == "não":
            break
        else:
            while continuar != "sim" or continuar != "não":
                print("Você digitou uma palavra diferente de sim ou não")
                continuar = input("Deseja continuar? sim ou não: ")
                if continuar == "não":
                    continuacao = False
                    break
                if continuar == "sim":
                    contador += 1
                    break
    else:
        print("Digite um número decimal.")

media = soma_notas / contador

print(contador)
print(f"A média das notas é {media}")

print("\n")
print("Prática 04: \n")

classificacao = ''
condicao_parada = 1
classificacao_leve = 0
classificacao_assintomatico = 0
classificacao_grave = 0
num_paciente = 1

while (condicao_parada != 0):
    classificacao = input("Digite a classificação do paciente " + str(num_paciente) + " (leve, assintomatico ou grave) para covid19")
    if (classificacao == 'leve'):
        classificacao_leve += 1
    elif (classificacao == 'assintomatico'):
        classificacao_assintomatico += 1
    else:
        classificacao_grave += 1
    condicao_parada = int(input("Se quiser parar digite 0 ou digite qualquer número para continuar"))
    if(condicao_parada != 0):
        num_paciente += 1



total_pacientes_registrados = num_paciente
percentual_leve = round(float((classificacao_leve * 100) / total_pacientes_registrados), 2)
percentual_assintomatico = round(float((classificacao_assintomatico * 100) / total_pacientes_registrados), 2)
percentual_grave = round(float((classificacao_grave * 100) / total_pacientes_registrados), 2)

print("O percentual de paciente com classificação leve é: " + percentual_leve)
print("O percentual de paciente com classificação assintomática é: " + percentual_assintomatico)
print("O percentual de paciente com classificação grave é: " + percentual_grave)

print("\n")
print("Prática 05: \n")

palavra_digitada = input("Digite uma palavra: ")
soma_vogais = 0

for i in palavra_digitada:
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        soma_vogais += 1
    else:
        continue

print (soma_vogais)