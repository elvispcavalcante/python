"""
Exercício 1 - Faça um programa que exiba um menu com as seguintes opções:
"""

condicao = True

while condicao:
    print("Digite a opção do que quer fazer:")
    print("Digite 1 para verificar se o número é par ou ímpar")
    print("Digite 2 calcular a área de um quadrado")
    print("Digite 3 calcular a área de um triângulo")
    print("Digite 4 para verificar se o número é positivo ou negativo")
    print("Digite 5 para sair")

    opcao = input("Qual a opção que você quer? ")

    if opcao.isnumeric() and int(opcao) <= 5 and int(opcao) > 0:
        opcao = int(opcao)
        if opcao == 1:
            print("Você selecinou a opção 1")
            numero = int(input("Digite um número: "))
            if numero % 2 == 0:
                print("O número digitado é par")
            else:
                print("O número digitado é ímpar")
        if opcao == 2:
            print("Você selecinou a opção 2")
            lado = int(input("Digite o lado do quadrado: "))
            print(f"A área do quadrado é {lado ** 2}")
        if opcao == 3:
            print("Você selecinou a opção 3")
            base = int(input("Digite a base do triângulo: "))
            altura = int(input("Digite a altura do triângulo: "))
            print(f"A área do triângulo é {(base * altura)/2}")
        if opcao == 4:
            print("Você selecinou a opção 4")
            numero = int(input("Digite um número: "))
            if numero < 0:
                print("O número digitado é negativo")
            else:
                print("O número digitado é positivo")
        if opcao == 5:
            print("Você saiu do programa")
            condicao = False

        import time
        time.sleep(3)
        print("\n" * 2)
    else:
        print("Você não digitou nenhuma opção exibidas!")

        import time
        time.sleep(1)
        print("\n" * 2)
        continue


# Calcule a média de notas informadas pelo usuário
qtde_notas = int(input("Digite a quantidade de notas que você quer preencher: "))
soma_notas = 0.0

for i in range(0, qtde_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma_notas += nota

print(f"A média das notas digitadas é {soma_notas / qtde_notas:.1f}")


# Realize uma pesquisa que classifique os pacientes com: sintomas leves, assintomáticos e sintomas graves. Ao final
# mostre o percentual de cada uma

qtde_pacientes = int(input("Digite a quantidade de pacientes: "))
sintomas_leves = 0
assintomaticos = 0
sintomas_graves = 0

for i in range(0, 10):
    print("Digite a condição do pacientes: Digite 1 para sintomas leves")
    print("Digite a condição do pacientes: Digite 2 assintomáticos")
    print("Digite a condição do pacientes: Digite 3 sintomas graves")
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        sintomas_leves += 1
    elif opcao == 2:
        assintomaticos += 1
    else:
        sintomas_graves += 1

print(f"O percentual de pacientes com sintomas leves é {((sintomas_leves * 100)/qtde_pacientes):.2f}%")
print(f"O percentual de pacientes assintomáticos é {((assintomaticos * 100)/qtde_pacientes):.2f}%")
print(f"O percentual de pacientes com sintomas graves é {((sintomas_graves * 100)/qtde_pacientes):.2f}%")


# Imprimir cada letra de uma palavra. Transformar todas as letras em minúscula
palavra = input("Digite uma palavra: ").lower()
vogais = 0

for i in palavra:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vogais += 1

print(f"A quantidade de vogais é {vogais}")

# Calcular o fatorial de número
numero = int(input("Digite um número que você queira saber o fatorial: "))
fatorial = 1
for i in range(numero, 1, -1):
    fatorial *= i

print(f"O número fatorial é {fatorial}")

# Contar a quantidade de votos de 3 candidatos a eleição
total_eleitores = int(input("Digite o total de eleitores: "))
candidato1 = 0
candidato2 = 0
candidato3 = 0

for i in range(0, total_eleitores):
    print("Digite em qual candidato quer votar")
    print("Digite 1 para o Candidato A")
    print("Digite 2 para o Candidato B")
    print("Digite 3 para o Candidato C")
    voto = int(input("Digite o seu voto: "))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    else:
        candidato3 += 1

    print(f"O percentual do candidato A é {((candidato1 * 100) / total_eleitores):.2f}%")
    print(f"O percentual do candidato B é {((candidato2 * 100) / total_eleitores):.2f}%")
    print(f"O percentual do candidato C é {((candidato3 * 100) / total_eleitores):.2f}%")
