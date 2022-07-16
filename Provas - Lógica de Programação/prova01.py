
# Calcular a quantidade de litros gastos em uma viagem
# Carro faz 12 km com um 1 litro

tempo_gasto = float(input("Digite a quantidade de horas gastas na viagem: "))
velocidade_media = float(input("Digite a velocidade média do carro durante a viagem: "))

distancia = tempo_gasto * velocidade_media
litros_usados = distancia / 12

print(f"A velocidade média é de {velocidade_media}")
print(f"O tempo gasto na viagem foi de {tempo_gasto}")
print(f"A distância percorrida foi de {distancia}km")
print(f"A quantidade de litros utilizada na viagem foi de {litros_usados:.2f} l")
