# Exercício Aula 01
# class Veiculo:
#     def __init__(self, marca: str, modelo: str, velocidadeMax: float, velocidadeAtual: float, ligado: bool, capacidade: int, tanque: float) -> None:
#         self.marca = marca
#         self.modelo = modelo
#         self.velocidadeMax = velocidadeMax
#         self.velocidadeAtual = velocidadeAtual
#         self.ligado = ligado
#         self.capacidade = capacidade
#         self.tanque = tanque
#
#     def ligar(self):
#         if self.ligado:
#             print('O veículo já está ligado!')
#         else:
#             self.ligado = True
#             print("O veículo está ligado")
#
#     def desligar(self):
#         if self.ligado == False:
#             print('O veículo já está desligado!')
#         else:
#             self.ligado = False
#             print("O veículo está desligado")
#
#     def acelerar(self, velocidade):
#         if self.ligado:
#             if self.velocidadeAtual + velocidade < self.velocidadeMax:
#                 self.velocidadeAtual += velocidade
#                 print(f'A velocidade atual do veículo depois de acelerar é {self.velocidadeAtual}')
#             else:
#                 print('Você já chegou na velocidade máxima do veículo')
#
#     def frear(self, percentual):
#         if self.velocidadeAtual - (self.velocidadeAtual * (percentual / 100)) >= 0:
#             self.velocidadeAtual -= (self.velocidadeAtual * (percentual / 100))
#             print(f'A velocidade do veículo foi reduzida para {self.velocidadeAtual}')
#         else:
#             print('O carro já não pode frear porque está parado.')
#
#     def exibirDados(self):
#         print(f'Marca: {self.marca}')
#         print(f'Modelo: {self.modelo}')
#         print(f'Velocidade Máxima: {self.velocidadeMax}')
#         print(f'Velocidade: {self.velocidadeAtual}')
#         print(f'Ligado: {self.ligado}')
#         print(f'Capacidade: {self.capacidade}')
#         print(f'Tanque: {self.tanque}')
#
#
# class Carro(Veiculo):
#     def __init__(self, marca, modelo, velocidadeMax, velocidadeAtual, ligado, capacidade, tanque, quantidade_portas:int, abs: bool):
#         super().__init__(marca, modelo, velocidadeMax, velocidadeAtual, ligado, capacidade, tanque)
#         self.quantidade_portas = quantidade_portas
#         self.abs = abs
#
#     def darARe(self, velocidade):
#         if self.velocidadeAtual - velocidade > -60 and self.velocidadeAtual == 0:
#             self.velocidadeAtual -= velocidade
#             print(f'A velocidade da marcha ré do carro é {self.velocidadeAtual}')
#         else:
#             print("Você atingiu a velocidade máxima da ré que é 60 km/h")
#
#     def exibirDadosCarro(self):
#         super().exibirDados()
#         print(f'Quantidade de Portas: {self.quantidade_portas}')
#         print(f'Abs: {self.abs}')
#
#
# class Moto(Veiculo):
#     def __init__(self, marca: str, modelo: str, velocidadeMax: float, velocidadeAtual: float, ligado: bool, capacidade: int, tanque: float, cilindradas: int) -> None:
#         super().__init__(marca, modelo, velocidadeMax, velocidadeAtual, ligado, capacidade, tanque)
#         self.cilindradas = cilindradas
#
#     def exibirDadosMoto(self):
#         super().exibirDados()
#         print(f'Cilindradas: {self.cilindradas}')
#
#
# carro = Carro('Chevrolet', 'Onix', 180.0, 0.0, False, 5, 50.0, 4, True)
# moto = Moto('Honda', 'XRE', 160.0, 0.0, False, 2, 18.0, 300)
#
# carro.ligar()
# carro.acelerar(100)
# print('---------------------')
# moto.ligar()
# moto.acelerar(60)
# print('---------------------')
# carro.frear(10)
# print('---------------------')
# moto.frear(10)
# print('---------------------')
#
# carro.exibirDadosCarro()
# print('---------------------')
# moto.exibirDadosMoto()
#
# print('---------------------')
# carro.desligar()
# print('---------------------')
# moto.desligar()


# from abc import ABC, abstractmethod
#
# class Pessoa:
#     def __init__(self, estado, renda):
#         self.estado = estado
#         self.renda = renda
#         self.imposto = 0.00
#
#     @abstractmethod
#     def declararImpostos(self):
#         pass
#
#
# class PessoaFisica(Pessoa):
#     def __init__(self, nome, cpf, data_nascimento, estado, renda):
#         self.nome = nome
#         self.cpf = cpf
#         self.data_nascimento = data_nascimento
#         super().__init__(estado, renda)
#
#     def declararImpostos(self):
#         if self.renda > 2000.00:
#             self.imposto = self.renda * 0.05
#             print(f'O valor de imposto da pessoa física de cpf {self.cpf} é {self.imposto}')
#         else:
#             self.imposto = 0.00
#             print(f'O valor de imposto da pessoa física de cpf {self.cpf} é {self.imposto}')
#
#
# class PessoaJuridica(Pessoa):
#     def __init__(self, cnpj, razao_social, nome_fantasia, estado, renda):
#         self.cnpj = cnpj
#         self.razao_social = razao_social
#         self.nome_fantasia = nome_fantasia
#         super().__init__(estado, renda)
#
#     def declararImpostos(self):
#         self.imposto = self.renda * 0.20
#         print(f'O valor de imposto da pessoa jurídica de cnpj {self.cnpj} é {self.imposto}')
#
#
#
# pfisica = PessoaFisica('Elvis', '111.111.111-11', '11/11/1111', 'CE', 3000.00)
# pjuridica = PessoaJuridica('11.111.111/0001-11', 'Visual Art Creative', 'Infinity School', 'CE', 100000.00)
#
#
# pfisica.declararImpostos()
# pjuridica.declararImpostos()

# from abc import ABC, abstractmethod
#
#
# class App:
#     def __init__(self, nome, consumo_memoria, consumo_bateria):
#         self.nome = nome
#         self.consumo_memoria = consumo_memoria
#         self.consumo_bateria = consumo_bateria
#
#
# class Smartphone:
#     def __init__(self, fabricante, memoria, bateria, consumo_memoria):
#         self.fabricante = fabricante
#         self.memoria = memoria
#         self.bateria = bateria
#         self.consumo_memoria = consumo_memoria
#         self.ligado = False
#         self.apps = []
#
#     def ligar(self):
#         if self.ligado:
#             print('O smartphone já está ligado')
#         else:
#             self.ligado = True
#             print('O smartphone ligou')
#
#     def desligar(self):
#         if self.ligado:
#             self.ligado = False
#             print('O smartphone desligou')
#         else:
#             print('O smartphone está desligado')
#
#     @abstractmethod
#     def abrirApp(self, nome_aplicativo, consumo_memoria, consumo_bateria):
#         pass
#
#     @abstractmethod
#     def fecharApp(self, nome_aplicativo):
#         pass
#
#     @abstractmethod
#     def listarApps(self):
#         pass
#
#     def exibirDados(self):
#         print('Sobre o Smartphone:')
#         print(f'Fabricante: {self.fabricante}')
#         print(f'Memória: {self.memoria}')
#         print(f'Bateria: {self.bateria}')
#         print(f'Consumo da Memória: {self.consumo_memoria}')
#         print(f'Ligado: {self.ligado}')
#         self.listarApps()
#
#
# class Xiaomi(Smartphone):
#     def __init__(self, fabricante, memoria, bateria, consumo_memoria):
#         super().__init__(fabricante, memoria, bateria, consumo_memoria)
#
#     def abrirApp(self, nome_aplicativo, consumo_memoria, consumo_bateria):
#         app = App(nome_aplicativo, consumo_memoria, consumo_bateria)
#         if self.consumo_memoria + consumo_memoria - consumo_memoria * 0.20 <= self.memoria and self.bateria > 0:
#             self.consumo_memoria = self.consumo_memoria + consumo_memoria - consumo_memoria * 0.20
#             self.apps.append(app)
#         else:
#             self.desligar()
#
#     def fecharApp(self, nome_aplicativo):
#         for aplicativo in self.apps:
#             if aplicativo.nome == nome_aplicativo:
#                 aplicacao = aplicativo
#                 if self.consumo_memoria - aplicativo.consumo_memoria > 0:
#                     self.consumo_memoria = self.consumo_memoria - aplicativo.consumo_memoria
#                 else:
#                     self.consumo_memoria = 0.00
#                 self.apps.remove(aplicacao)
#         self.bateria = self.bateria - (self.bateria * 0.005)
#
#     def listarApps(self):
#         if len(self.apps) > 0:
#             self.bateria = self.bateria - (self.bateria * 0.005)
#             print("Na memória do smartphone tem os seguintes aplicativos: ")
#             for app in self.apps:
#                 print(f"Nome: {app.nome}, Consumo Memória: {app.consumo_memoria}, Consumo Bateria: {app.consumo_bateria}")
#         else:
#             print('Aplicativos:')
#             print('Não há aplicativos na memória no momento!')
#
#
# class Iphone(Smartphone):
#     def __init__(self, fabricante, memoria, bateria, consumo_memoria):
#         super().__init__(fabricante, memoria, bateria, consumo_memoria)
#
#     def abrirApp(self, nome_aplicativo, consumo_memoria, consumo_bateria):
#         app = App(nome_aplicativo, consumo_memoria, consumo_bateria)
#         if self.consumo_memoria + consumo_memoria + consumo_memoria * 0.20 <= self.memoria and self.bateria > 0:
#             self.consumo_memoria += consumo_memoria + (consumo_memoria * 0.20)
#             self.apps.append(app)
#         else:
#             self.desligar()
#
#     def fecharApp(self, nome_aplicativo):
#         for aplicativo in self.apps:
#             if aplicativo.nome == nome_aplicativo:
#                 aplicacao = aplicativo
#                 self.consumo_memoria -= aplicativo.consumo_memoria
#                 self.apps.remove(aplicacao)
#         self.bateria -= self.bateria * 0.01
#
#     def listarApps(self):
#         self.bateria -= self.bateria * 0.01
#         print("Na memória do smartphone tem os seguintes aplicativos: ")
#         for app in self.apps:
#             print(f"Nome: {app.nome}, Consumo Memória: {app.consumo_memoria}, Consumo Bateria: {app.consumo_bateria}")
#
#
# xiaomi = Xiaomi('Xiaomi', 100, 100, 0)
# iphone = Iphone('Iphone', 200, 100, 0)
#
# xiaomi.ligar()
# xiaomi.abrirApp('Camera', 20, 20)
# xiaomi.listarApps()
# xiaomi.exibirDados()
# xiaomi.fecharApp('Camera')
# xiaomi.exibirDados()
# xiaomi.desligar()
#
# iphone.ligar()
# iphone.abrirApp('Camera', 20, 20)
# iphone.listarApps()
# iphone.exibirDados()
# iphone.fecharApp('Camera')
# iphone.exibirDados()
# iphone.desligar()

from abc import ABC, abstractmethod


class Conta:
    def __init__(self, num_conta, titular, saldo):
        self.num_conta = num_conta
        self.titular = titular
        self.saldo = saldo

    @abstractmethod
    def sacar(self):
        pass

    @abstractmethod
    def depositar(self):
        pass


class ContaCorrente(Conta):
    def __init__(self, num_conta, titular, saldo, limite_cheque_especial):
        super().__init__(num_conta, titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def sacar(self, valor):
        if self.saldo + self.limite_cheque_especial >= valor:
            self.saldo -= valor
            print(f'O valor de R$ {valor} foi sacado do seu saldo. O saldo atual é R$ {self.saldo} ')
        else:
            print(f'Não temos limite para efetuar o saque')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'O valor de R$ {valor} foi depositado no sua conta. O saldo atual é R$ {self.saldo} ')
        else:
            print(f'Não é possível depositar o valor repassado!')


# noinspection PyMethodOverriding
class ContaPoupanca(Conta):
    def __init__(self, num_conta, titular, saldo, rendimento):
        super().__init__(num_conta, titular, saldo)
        self.rendimento = rendimento

    def sacar(self, valor):
        if self.saldo > valor:
            self.saldo -= valor
            print(f'O valor de R$ {valor} foi sacado do seu saldo. O saldo atual é R$ {self.saldo} ')
        else:
            print(f'Não temos limite para efetuar o saque')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'O valor de R$ {valor} foi depositado no sua conta. O saldo atual é R$ {self.saldo} ')
        else:
            print(f'Não é possível depositar o valor repassado!')

    def calcularRendimento(self):
        rendimento_gerado = float((self.saldo * (self.rendimento / 100)))
        self.saldo = float(self.saldo) + rendimento_gerado
        print(f'Você teve um rendimento de R$ {rendimento_gerado}')
        print(f'O seu saldo atual agora é de R$ {self.saldo}')


# contaCorrente = ContaCorrente('321-X', 'Elvis', 1000, 200)
# contaCorrente.sacar(1500)
# contaCorrente.depositar(100)

contaPoupanca = ContaPoupanca('123-x', 'Elvis', 2000.00, 10.00)

contaPoupanca.depositar(100)
contaPoupanca.sacar(100)
contaPoupanca.calcularRendimento()



