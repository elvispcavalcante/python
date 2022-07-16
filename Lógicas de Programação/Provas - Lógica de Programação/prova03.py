# Frete grátis a partir de 200,00 reais

soma_produtos = 0.0
continuacao = True

while continuacao:
    valor_produto = float(input("Digite o valor do produto: "))
    continua = input("Quer digitar mais um valor de um produto? Digite sim ou não: ")

    if continua == "não":
        soma_produtos += valor_produto
        break
    elif continua == "sim":
        soma_produtos += valor_produto
    else:
        while continua != 'sim' or continua != 'não':
            print("Você digitou outras opções para continuar ou parar. Digite sim ou não")
            continua = input("Quer digitar mais um valor de um produto? Digite sim ou não: ")
            if continua == "não":
                soma_produtos += valor_produto
                continuacao = False
                break
            elif continua == "sim":
                soma_produtos += valor_produto
                break

print(f"A soma do valor dos produtos que você digitou é de R$ {soma_produtos:.2f} ")
if soma_produtos >= 200.00:
    print(f"O frete da compra que você realizou é GRÁTIS. Parabéns!!")
else:
    print("O valor do frete precisa ser calculado de acordo com o seu endereço!")