# Exercícios slides da aula 02

"""
Lembrando de comentários em bloco
"""


print("Prática 01: \n")

numero = int(input("Por favor digite um número:"))

if (numero <= 0):
    print("O número é negativo \n")
else:
    print("O número é positivo \n")

print("Prática 02: \n")

"""
temperatura <= 37 - normal
temperatura <= 34 - hipotermia
temperatura > 37 - febre
"""

cancela = False
mensagem = ""
afericao_temperatura = float(input("Verifique a sua temperatura:"))

if(afericao_temperatura <= 34.0):
    cancela = True
    mensagem = "Procure um médico pois está com hipotermia."
elif(afericao_temperatura > 37.0):
    cancela = False
    mensagem = "Temperatura maior que 37 graus. Você está com febre."
else:
    cancela = True
    mensagem = "Seja bem-vindo(a)!"

if (cancela == True):
    print("Cancela liberada", mensagem, sep = ' - ')
    print("\n")
else:
    print("Cancela não liberada", mensagem, sep = ' - ')
    print("\n")

print("Prática 03: \n")

hosp1_respiradores = int(input("Digite a quantidade de respiradores:"))
hosp1_percentual_ocupacao = float(input("Digite o percentual de ocupação sem o símbolo de %"))

hosp2_respiradores = int(input("Digite a quantidade de respiradores:"))
hosp2_percentual_ocupacao = float(input("Digite o percentual de ocupação sem o símbolo de %"))

hosp3_respiradores = int(input("Digite a quantidade de respiradores:"))
hosp3_percentual_ocupacao = float(input("Digite o percentual de ocupação sem o símbolo de %"))

hosp4_respiradores = int(input("Digite a quantidade de respiradores:"))
hosp4_percentual_ocupacao = float(input("Digite o percentual de ocupação sem o símbolo de %"))

hosp5_respiradores = int(input("Digite a quantidade de respiradores:"))
hosp5_percentual_ocupacao = float(input("Digite o percentual de ocupação sem o símbolo de %"))

if(hosp1_respiradores < 50 and hosp1_percentual_ocupacao > 60):
    hosp1_respiradores += 5
if(hosp2_respiradores < 50 and hosp2_percentual_ocupacao > 60):
    hosp2_respiradores += 5
if(hosp3_respiradores < 50 and hosp3_percentual_ocupacao > 60):
    hosp3_respiradores += 5
if(hosp4_respiradores < 50 and hosp4_percentual_ocupacao > 60):
    hosp4_respiradores += 5
if(hosp5_respiradores < 50 and hosp5_percentual_ocupacao > 60):
    hosp5_respiradores += 5

print("Quantidade de respiradores do hospital 01 é:", hosp1_respiradores)
print("Quantidade de respiradores do hospital 02 é:", hosp2_respiradores)
print("Quantidade de respiradores do hospital 03 é:", hosp3_respiradores)
print("Quantidade de respiradores do hospital 04 é:", hosp4_respiradores)
print("Quantidade de respiradores do hospital 05 é:", hosp5_respiradores)
print("\n")


print("Prática 04: \n")

"""
existem 3 grupos de industrías
poluicao entre 0,05 e 0,25 é aceitável
poluicao com 0,3 as atividades são suspensas do 1º grupo
poluicao com 0,4  as atividades são suspensas do 1º e 2º grupo
poluicao com 0,5 as atividades dos 3º grupo são suspensas
"""

indice_poluicao = float(input('Informe o índice de poluição (Na casa decimal utilize "." ): '))

if(indice_poluicao < 0):
    print("Digite um índice maior do que 0.")
elif(indice_poluicao < 0.05):
    print("A poluição é zero ou próximo disso")
elif(indice_poluicao >= 0.05 and indice_poluicao <= 0.29):
    print("A poluição existente é aceitável")
elif(indice_poluicao >= 0.3 and indice_poluicao < 0.4):
    print("As atividades das indústrias do grupo 01 devem ser suspensas")
elif(indice_poluicao >= 0.4 and indice_poluicao < 0.5):
    print("As atividades das indústrias do grupo 01 e 02 devem ser suspensas")
else:
    print("As atividades das indústrias do grupo 01, 02 e 03 devem ser suspensas")

print("\n")
print("Prática 05: \n")

time1 = input("Digite o nome do time 1:")
gol_marcado_time_1 = int(input("Digite o número de gols marcado pelo time 1 na partida: "))
time2 = input("Digite o nome do time 2:")
gol_marcado_time_2 = int(input("Digite o número de gols marcado pelo time 2 na partida: "))

if(gol_marcado_time_1 < 0 or gol_marcado_time_2 < 0):
    print("Digite novamente os valares pois não existe número negativo de gols na partida")
elif(gol_marcado_time_1 > gol_marcado_time_2):
    print("O vencedor é o " + time1 + ". Fez " + str(gol_marcado_time_1) + " gols enquanto o time do " + time2 + " fez " + str(gol_marcado_time_2) +
          " gols")
elif (gol_marcado_time_2 > gol_marcado_time_2):
    print("O vencedor é o "+ time2 + ". Fez " + str(gol_marcado_time_2) + " gols enquanto o time do " + time1 + " fez " + str(gol_marcado_time_1) +
          " gols")
else:
    print("Não houve vencedor. Empate!")

print("\n")
print("Prática 06: \n")

codigo = input("Digite o código (matrícula) do empregado: ")
ano_nascimento = int(input("Digite o ano de nascimento do empregado: "))
ano_ingresso = int(input("Digite o ano de ingresso (admissão) do empregado: "))

from datetime import datetime
data_atual = datetime.today()
ano_data_atual = int(data_atual.year)

idade = ano_data_atual - ano_nascimento
tempo_trabalhado = ano_data_atual - ano_ingresso

if(idade >= 65):
    print("O empregado deve requerer aposentadoria. Possui idade igual ou superior a 65 anos. Sua idade é de: " + str(idade) + " anos e "
     "o seu tempo trabalhado na empresa é de " + str(tempo_trabalhado) + " anos.")
elif(tempo_trabalhado >= 30):
    print("O empregado deve requerer aposentadoria. Possui tempo de trabalho igual ou superior a 30 anos. O seu tempo "
          "trabalhado na empresa é de " + str(tempo_trabalhado) + " anos. " + "Sua idade é de: " + str(idade) + " anos.")
elif(idade >= 60 and tempo_trabalhado >= 25):
    print("O empregado deve requerer aposentadoria. Possui tempo de trabalho igual ou superior a 25 anos e a sua idade é maior do que"
          "60 anos. O seu tempo trabalhado na empresa é de " + str(tempo_trabalhado) + " anos. " + "Sua idade é de: " + str(idade) + " anos.")
else:
    print("O empregado não possui os critérios necessários para requerer aposentadoria. Sua idade é " + str(idade) + " anos. O seu tempo"
    " trabalhado na empresa é de " + str(tempo_trabalhado) + " anos.")

print("\n")
print("Prática 07: \n")

produto1 = float(input("Digite o valor do produto 01: "))
produto2 = float(input("Digite o valor do produto 02: "))
produto3 = float(input("Digite o valor do produto 03: "))

if((produto1 < produto2) and (produto1 < produto3)):
    print("Produto 1 é o mais barato e deve ser comprado")
elif((produto2 < produto1) and (produto2 < produto3)):
    print("Produto 2 é o mais barato e deve ser comprado")
elif((produto3 < produto1) and (produto3 < produto2)):
    print("Produto 3 é o mais barato e deve ser comprado")
else:
    print("Verificar problema nos produtos apresentados")



