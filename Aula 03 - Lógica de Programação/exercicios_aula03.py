# 1º Exercício


numero = int(input("Digite um número: "))

for i in range(0, numero + 1):
    print(i)

# 2º exercício:
contador = 1
qtd_pares = 0
qtd_impares = 0

while contador <= 10:
    numero = int(input("Digite o número "+str(contador)+":"))

    if numero % 2 == 0:
        qtd_pares += 1
    else:
        qtd_impares += 1

    contador += 1

print("A quantidade de números pares é: ", qtd_pares)
print("A quantidade de números ímpares é: ", qtd_impares)

# 3º exercício:

numero_tabuada = int(input("Digite o número da tabuada que queira visualizar: "))

for i in range(1, 11):
    print(f"{numero_tabuada} X {i} = {numero_tabuada * i}")

# 4º Exercício

contador = 1
soma_notas = 0
while contador <= 3:
    nota = float(input("Digite a nota: "))
    soma_notas += nota
    contador += 1

print(f"A média do aluno é {soma_notas / contador}")

import random

numero_sorteado = random.randrange(1, 10)
numero_escolhido = 0

while True:
    numero_escolhido = int(input("Escolha um número de 1 a 10: "))

    if numero_escolhido > 10 or numero_escolhido < 1:
        print("Você digitou um número diferente de 1 a 10")
        continue
    elif numero_escolhido < numero_sorteado:
        print("O número escolhido é menor do que o númeroo sorteado")
        continue
    elif numero_escolhido > numero_sorteado:
        print("O número escolhido é maior do que o número sorteado")
        continue
    else:
        print("Acertoooouuuu! O número escolhido é igual ao sorteado")
        break

print(f"O número sorteado foi {numero_sorteado}")
print(f"O número escolhido foi {numero_escolhido}")

# 5º exercício

import random

numero_sorteado = random.randrange(1, 10)
numero_escolhido = 0

while True:
    numero_escolhido = int(input("Escolha um número de 1 a 10: "))

    if numero_escolhido > 10 or numero_escolhido < 1:
        print("Você digitou um número diferente de 1 a 10")
        continue
    elif numero_escolhido < numero_sorteado:
        print("O número escolhido é menor do que o númeroo sorteado")
        continue
    elif numero_escolhido > numero_sorteado:
        print("O número escolhido é maior do que o número sorteado")
        continue
    else:
        print("Acertoooouuuu! O número escolhido é igual ao sorteado")
        break

print(f"O número sorteado foi {numero_sorteado}")
print(f"O número escolhido foi {numero_escolhido}")

# 6º Exercício
"""
5. Foi feita uma pesquisa entre os habitantes de uma região. foram coletados os dados de idade,
sexo (M/F) e salário. Faça um programa que calcule e mostre:

a) A média dos salários do grupo;
b) A maior e a menor idade do grupo;
c) A quantidade de mulheres na região;
d) A idade e o sexo da pessoa que possui o menor salário

Finalize a entrada de dados ao ser digitada uma idade negativa


"""

soma_salarios = 0
qtde_digitada = 0
menor_idade = 150
maior_idade = 0
qtde_mulheres = 0
menor_salario = 99999999999
sexo_menor_salario = ''
idade_menor_salario = 0

while True:

    idade = int(input("Digite a idade. Se idade for negativa o programa será terminado: "))
    if idade < 0:
        break

    sexo = input("Digite o sexo. Digite m ou f")
    salario = float(input("Digite o salário"))

    if idade < menor_idade:
        menor_idade = idade
    if idade > maior_idade:
        maior_idade = idade

    if sexo == 'f':
        qtde_mulheres += 1

    soma_salarios += salario
    qtde_digitada += 1

    if salario < menor_salario:
        sexo_menor_salario = sexo
        idade_menor_salario = idade

    continuar = input("Deseja continuar? s ou n ")
    if continuar == 'n':
        break

print(f"A media de salários {soma_salarios / qtde_digitada}")
print(f"A maior idade do grupo {maior_idade}")
print(f"A menor idade do grupo {menor_idade}")
print(f"A quantidade de mulheres da regiao {qtde_mulheres}")
print(f"A idade do menor salário é {idade_menor_salario} e o sexo do menor salário é {sexo_menor_salario}")