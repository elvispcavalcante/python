import random


class Pessoa:
    def __init__(self, nome, sexo, cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf


#pessoa = Pessoa("Fernando", "Masculino", "032.312.123-21")


lista_objetos = []
for i in range(0,3):
    nome = "Fernando"
    sexo = random.randrange(0, 2)
    if sexo == 0:
        sexo = "Masculino"
    else:
        sexo = "Feminino"
    cpf = random.randrange(11111111111, 99999999999)
    pessoa = Pessoa(f"{nome} {i}", sexo, cpf)
    lista_objetos.append(pessoa)

print(lista_objetos)

for item in lista_objetos:
    print("-------------")
    print(item.nome)
    print(item.sexo)
    print(item.cpf)