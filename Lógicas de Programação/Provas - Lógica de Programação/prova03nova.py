soma = 0
qtd_numeros = 0

while True:
    numero = int(input("Digite um número: "))

    soma += numero
    qtd_numeros += 1

    continuar = input("Quer continuar? Digite s ou n: ")

    if continuar == 's':
        continue
    else:
        break

print(f"A soma dos números digitados é {soma}")
print(f"A média dos números digitados é {soma/qtd_numeros:.2f}")