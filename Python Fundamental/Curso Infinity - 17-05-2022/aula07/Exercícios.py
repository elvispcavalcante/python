class Carro:
    def __init__(self, marca:str, modelo:str, ano:int, automatico:bool, ligado=False, velocidade = 0.0):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__velocidade = velocidade
        self.__automatico = automatico
        self.__ligado = ligado

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def ano(self):
        return self.__ano

    @property
    def velocidade(self):
        return self.__velocidade

    @property
    def automatico(self):
        return self.__automatico

    @property
    def ligado(self):
        return self.__ligado

    def ligar(self):
        if self.__ligado == True:
            print("O carro já está ligado!")
        else:
            self.__ligado = True
            print("O carro está ligado!")

    def desligar(self):
        if self.__ligado == False:
            print("O carro já está desligado!")
        else:
            self.__ligado = False
            print("O carro está desligado!")

    def acelerar(self, velocidade_aumentar):
        if self.__velocidade + velocidade_aumentar > 120:
            self.__velocidade = 120
            print("Você atingiu a velocidade máxima")
            self.verificarMarcha()
            return self.__velocidade
        else:
            self.__velocidade += velocidade_aumentar
            self.verificarMarcha()
            return self.__velocidade

    def reduzir(self, velocidade_diminuir):
        if self.__velocidade - velocidade_diminuir < 0:
            self.__velocidade = 0
            print("Você atingiu a velocidade mínima")
            self.verificarMarcha()
            return self.__velocidade
        else:
            self.__velocidade -= velocidade_diminuir
            self.verificarMarcha()
            return self.__velocidade

    def verificarMarcha(self):
        if self.__velocidade >= 0 and self.__velocidade < 20:
            print(f"A sua velocidade é {self.__velocidade}")
            print("Você está na 1ª marcha")
        elif self.__velocidade >= 20 and self.__velocidade < 30:
            print(f"A sua velocidade é {self.__velocidade}")
            print("Você está na 2ª marcha")
        elif self.__velocidade >= 30 and self.__velocidade < 35:
            print(f"A sua velocidade é {self.__velocidade}")
            print("Você está na 3ª marcha")
        elif self.__velocidade >= 35 and self.__velocidade < 50:
            print(f"A sua velocidade é {self.__velocidade}")
            print("Você está na 4ª marcha")
        elif self.__velocidade >= 50:
            print(f"A sua velocidade é {self.__velocidade}")
            print("Você está na 5ª marcha")
        else:
            print("A velocidade é inválida")

# Foi utilizado como opcional a velocidade e o atributo ligado
carro = Carro("Chevrolet", "Cruze", "2022", True)

#Ligar o carro
carro.ligar()

#Teste ao mandar ligar novamente
carro.ligar()

#Teste acelerar a velocidade do carro
carro.acelerar(10)
carro.acelerar(10)
carro.acelerar(10)
carro.acelerar(10)
carro.acelerar(10)
carro.acelerar(30)
carro.acelerar(30)
carro.acelerar(30)

#Teste reduzir velocidade do carro
carro.reduzir(10)
carro.reduzir(30)
carro.reduzir(30)
carro.reduzir(20)
carro.reduzir(20)
carro.reduzir(15)

print("")
#teste ligar o carro
carro.desligar()
#teste carro já desligado
carro.desligar()


