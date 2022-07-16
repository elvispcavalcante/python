#Forma Tradicional
print("Olá, mundo!")

#1ª Forma
print("O", "l", 'á', ',', sep="", end=" ")
print("m", "u", "n", "d", "o", "!", sep="")

#2ª forma
def codigoInicialDoProgramador():
    print("Olá, mundo!")

codigoInicialDoProgramador()

#3ª forma
msg = "!odnum ,álO"
msg_nova = ''

for i in range(len(msg)-1, -1, -1):
    msg_nova += msg[i]

print(msg_nova)

#4ªforma
letras_alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(letras_alfabeto[14].capitalize() + letras_alfabeto[11] + letras_alfabeto[0].replace("a", "á"), end=", ")
print(letras_alfabeto[12] + letras_alfabeto[20] + letras_alfabeto[13] + letras_alfabeto[3] + letras_alfabeto[14], end="!\n")

#5ª forma
msg = "Bem vindo a Infinity School! Se você é programador existe um ritual para iniciar uma nova linguagem. É criar o código: Olá, mundo!"
contador = 0
olaMundo = ''
while contador <= len(msg) - 1:
    if msg[contador] == 'O':
        olaMundo += msg[contador]
        if msg[contador + 1] == 'l':
            olaMundo += msg[contador + 1]
            if msg[contador + 2] == 'á':
                olaMundo += msg[contador + 2]
                if msg[contador + 3] == ',':
                    olaMundo += msg[contador + 3]
                    if msg[contador + 4] == ' ':
                        olaMundo += msg[contador + 4]
                        if msg[contador + 5] == 'm':
                            olaMundo += msg[contador + 5]
                            if msg[contador + 6] == 'u':
                                olaMundo += msg[contador + 6]
                                if msg[contador + 7] == 'n':
                                    olaMundo += msg[contador + 7]
                                    if msg[contador + 8] == 'd':
                                        olaMundo += msg[contador + 8]
                                        if msg[contador + 9] == 'o':
                                            olaMundo += msg[contador + 9]
                                            if msg[contador + 10] == '!':
                                                olaMundo += msg[contador + 10]
                                                break
    else:
        contador += 1

print(olaMundo)


