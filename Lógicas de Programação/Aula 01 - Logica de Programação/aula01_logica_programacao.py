# Este é um comentário de uma linha
"""
Este é um comentário em bloco
"""
'''
Este é um comentário em bloco
'''

# Função sep para separar parâmetros. Com ela você pode alterar como strings, por exemplo, podem ser alteradas
# Função end para mudar o caractere que será usada entre dois prints, por exemplo. Altero o final da primeira string para juntar com a segunda string

# Variáveis
"""
integer => Forma de criação => b = 12
String => Forma de criação => nome = "teste"
float => Forma de criação => x = 19.6 
boolean => Forma de criação => aprovado = true
"""

#Operadores

"""
+ -> adição
- -> subtração
* -> multiplicação
/ -> divisão
// -> divisão inteira
** -> potenciação
% -> módulo ou resto da divisão
() -> Precedência da operação

"""

#Início da aula 01

print("Hello 'World'") # Esta linha imprime o 'Hello World'

#Utilização do sep e end
print("Olá, bem vindos a", "Infinity School", sep="###")

print("Olá, bem vindos a", end="$$$$")
print("Infinity School", end="@@@@@@")
print("A mais top")

""" 735.622.050-40"""

print("735", "622", "050", sep=".", end="-"+"40\n")

#código para montar a máscara do CPF utilizando str (substring)
# cpf = "73562205040"
cpf = input("Digite somente o número do seu CPF")

parte1cpf = str(cpf[0:3])
parte2cpf = str(cpf[3:6])
parte3cpf = str(cpf[6:9])
parte4cpf = str(cpf[9:11])

print(parte1cpf, parte2cpf, parte3cpf, sep=".", end="-"+parte4cpf)

#Exemplos de operadores

idade = 19

soma = idade + 5
subtracao = idade - 4
multiplicacao = idade * 2
divisao = idade / 2
divisaoInteira = idade // 2
potenciacao = 2 ** 3
modulo = idade % 2
precedencia = (idade + 2) * 2

print("\n \n")
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisaoInteira)
print(potenciacao)
print(modulo)
print(precedencia)


print("\n Exercício sobre variáveis")
#Exercício01
print("\n Exercício 01:")
altura = 1.80
peso = 90
imc = round(peso / (altura * altura), 2)
print("O seu IMC é", imc)

print("\n Exercício 02: ")
nota1 = 10
nota2 = 8
nota3 = 6
media = (nota1 + nota2 + nota3) / 3

print("A média do aluno é", media)

print("\n Exercício 03:")

ladoQuadrado = 15
areaQuadrado = ladoQuadrado * ladoQuadrado

print("Lado do quadrado:", ladoQuadrado)
print("Área do quadrado:", areaQuadrado)

print("\n Exercício 04:")
baseTriangulo = 10
alturaTriangulo = 3
areaTriangulo = (baseTriangulo * alturaTriangulo) / 2

print("Base do Triângulo", baseTriangulo)
print("Altura do Triângulo", alturaTriangulo)
print("Área do Triângulo", areaTriangulo)



