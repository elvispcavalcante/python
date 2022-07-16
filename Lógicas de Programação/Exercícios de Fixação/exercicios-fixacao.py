#Questão 01

num_metros = (input("Digite um número em metros para ser convertido para centímetros: "))
num_centimetros = 0

if (num_metros.replace('.', '')).isnumeric():
    num_centimetros = float(num_metros) * 100
    print(f"O número digitado convertido em centímetros é {num_centimetros}")
else:
    print("Você não digitou um número!")

#Questão 02

raio = float(input("Digite o raio do círculo: "))
pi = 3.14

area_circulo = pi * (raio ** 2)
print(f"Á área do círculo é igual a {area_circulo}")

#Questão 03

import math

raio = float(input("Digite o raio do círculo: "))
pi = math.pi

area_circulo = round(pi * (raio ** 2),2)
print(f"Á área do círculo é igual a {area_circulo}")

#Questão 04

temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

temperatura_celsius = 5 * ((temperatura_fahrenheit - 32) / 9)

print(f"A temperatura em Celsius é t{temperatura_celsius}")

#Questão 05

temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

temperatura_fahrenheit = round(((temperatura_celsius * 9)/5)+32,1)

print(f"A temperatura em fahrenheit é {temperatura_fahrenheit}")

#Questão 06

print(10)

#Questão 07

numero = 7
print(numero)

#Questão 08

numero = input("Digite um número: ")

if numero.isnumeric():
    print("O número digitado foi", int(numero))
else:
    print("Você não digitou um número!")

#Questão 09

numero1 = float(input("Digite o número 01: "))
numero2 = float(input("Digite o número 02: "))

print(f"A soma dos números é {numero1 + numero2}")

#Questão 10

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4)/4

print(f"A nota 1 é {nota1}")
print(f"A nota 2 é {nota2}")
print(f"A nota 3 é {nota3}")
print(f"A nota 4 é {nota4}")
print(f"A média das notas é {media}")

#Questão 11
"""
1 litro faz 3 metros quadrados
uma lata de tinta tem 18 litros
uma lata de tinta é R$ 80,00
"""
from math import ceil

area_a_ser_pintada = float(input(" Digite a área, em metros quadrados, a ser pintada: "))

#ceil -> arredondar para cima
qtde_latas_tinta = ceil((((area_a_ser_pintada * 1)/3)/18))

preco_total = 80.00 * qtde_latas_tinta

print("A quantidade de latas de tinta a ser comprada é", qtde_latas_tinta)
print("O valor do preço total a ser pago é", preco_total)

#Questão 12

velocidade_km_hora = float(input("Digite a velocidade em km/h para ser convertida em m/s: "))

velocidade_m_por_segundo = round((velocidade_km_hora / 3.6), 2)

print(f"A velocidade em metros por segundo é {velocidade_m_por_segundo} m/s")

#Questão 13

velocidade_m_por_segundo = float(input("Digite a velocidade em km/h para ser convertida em km/h: "))

velocidade_km_hora = round((velocidade_m_por_segundo * 3.6), 2)

print(f"A velocidade em quilômetros por hora é {velocidade_km_hora} km/h")

#Questão 14

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

print("A soma desses números é ", num1 + num2 + num3)

#Questão 15

salario= float(input("Digite o seu salário: "))
reajuste = 25.00
salario_reajustado = salario + ((salario * reajuste)/100)

print(f"O seu salário foi reajustado em {reajuste}%. Seu novo salário é R$ {salario_reajustado:.2f}")

#Questão 16

premio = 540000.00
pessoa1 = input("Digite o nome da pessoa: ")
pessoa2 = input("Digite o nome da pessoa: ")
pessoa3 = input("Digite o nome da pessoa: ")

print(f"{pessoa1} vai receber {round(premio / 3,2)}")
print(f"{pessoa2} vai receber {round(premio / 3,2)}")
print(f"{pessoa3} vai receber {round(premio / 3,2)}")

#Questão 17

premio = 540000.00
pessoa1 = input("Digite o nome da pessoa: ")
pessoa2 = input("Digite o nome da pessoa: ")
pessoa3 = input("Digite o nome da pessoa: ")

print(f"{pessoa1} vai receber {round((premio * 47)/100,2)}")
print(f"{pessoa2} vai receber {round((premio * 31)/100,2)}")
print(f"{pessoa3} vai receber {round((premio * 22)/100,2)}")

#Questão 18

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
num3 = float(input("Digite um número real: "))

print(f"O produto do dobro do primeiro com a metade do segundo é {(num1 * 2) * (num2 / 2)}")
print(f"A soma do triplo do primeiro com o terceiro é {(num1 * 3) + num3}")
print(f"O terceiro elevado ao cubo é {num3 ** 3}")

#Questão 19

num1 = int(input("Digite um número inteiro: "))
num2 = float(input("Digite um número float: "))
texto = input("Digite um texto: ")

print(f"O tipo da variável 1 é ", type(num1))
print(f"O tipo da variável 2 é ", type(num2))
print(f"O tipo da variável 3 é ", type(texto))

#Questão 20

num1 = int(input("Digite um número inteiro: "))

print(f"O valor do módulo da divisão por 2 é", num1 % 2)
