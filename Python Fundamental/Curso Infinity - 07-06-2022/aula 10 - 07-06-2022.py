# class Escola:
#     def __init__(self, nome, endereco):
#         self.nome = nome
#         self.endereco = endereco
#         self.cursos = ['Dev FullStack', 'Data Science']
#         self.alunos = []
#
#     def matricularAluno(self, aluno):
#         self.alunos.append(aluno)
#
#     def exibirAlunos(self):
#         print(f'Na Escola {self.nome}, no endereço {self.endereco}, estão matriculados os seguintes alunos: ')
#         for i in range(len(self.cursos)):
#             print(f'No Curso de {self.cursos[i]}: ')
#             for aluno in self.alunos:
#                 if aluno.curso == self.cursos[i]:
#                     print(f'Aluno: {aluno.nome}, Matrícula: {aluno.matricula}, Idade: {aluno.idade}, Curso: {aluno.curso}')
#                 else:
#                     pass
#
#
# class Aluno:
#     def __init__(self, matricula, nome, idade, curso):
#         self.matricula = matricula
#         self.nome = nome
#         self.idade = idade
#         self.curso = curso
#
#
# aluno1 = Aluno('123', 'Elvis', 35, 'Dev FullStack')
# aluno2 = Aluno('321', 'Junior', 32, 'Dev FullStack')
# aluno3 = Aluno('125', 'Diego', 26, 'Data Science')
# aluno4 = Aluno('245', 'Carlos', 25, 'Dev FullStack')
# aluno5 = Aluno('987', 'Samay', 19, 'Designer')
#
# escola = Escola('Infinity School', 'Av. Santos Dumont, Aldeota')
#
# escola.matricularAluno(aluno1)
# escola.matricularAluno(aluno2)
# escola.matricularAluno(aluno3)
# escola.matricularAluno(aluno4)
# escola.matricularAluno(aluno5)
#
# escola.exibirAlunos()


# #Exercício 01 e 02
# class Funcionario:
#     def __init__(self, matricula, nome, salario):
#         self.matricula = matricula
#         self.nome = nome
#         self.salario = salario
#         self.horas_estagiadas = 0
#
#
# class Estagiario(Funcionario):
#     def __init__(self, matricula, nome, salario,):
#         super().__init__(matricula, nome, salario)
#         self.horas_estagiadas = 0
#
#     def contratacao(self, horas):
#         if self.horas_estagiadas + horas > 300:
#             self.horas_estagiadas += horas
#             print(f'Você será contratado porque já estagiou {self.horas_estagiadas} horas')
#         else:
#             print(f'O estágio ainda não acabou')
#
#
# class Gerente(Funcionario):
#     def __init__(self, matricula, nome, salario, setor, comissao):
#         super().__init__(matricula, nome, salario)
#         self.setor = setor
#         self.comissao = comissao
#         self.qtde_funcionarios = 0
#
#     def contratar(self, quantidade):
#         if quantidade < 10 and self.qtde_funcionarios < 10:
#             self.qtde_funcionarios += quantidade
#             print(f'Serão contratados {quantidade} funcionários')
#         else:
#             print(f'O setor já possui tem gente suficiente')
#
#
# funcionario = Funcionario('321', 'Elvis', 3500.00)
# print(funcionario.nome)
# print(funcionario.matricula)
# print(funcionario.salario)
#
# estagiario = Estagiario('123', 'Leandro', 600.00)
# print(estagiario.nome)
# print(estagiario.matricula)
# print(estagiario.salario)
# estagiario.contratacao(400)
#
# gerente = Gerente('456', 'Daniel', 3500.00, 'Financeiro', 500.00)
# print(gerente.nome)
# print(gerente.matricula)
# print(gerente.salario)
# print(gerente.setor)
# print(gerente.comissao)
# gerente.contratar(10)
#
#Exercício 03
class Conta:
    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo - valor > 0:
            self.saldo -= valor
            print('Saque realizado com sucesso!')
        else:
            print('Você não possui saldo suficiente para realizar o saque!')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print('Depósito realizado com sucesso!')
        else:
            print('O valor não pode ser menor ou igual a 0!')


class ContaCorrente(Conta):
    def __init__(self, numero, nome, limite_cheque_especial):
        super().__init__(numero, nome)
        self.limite_cheque_especial = limite_cheque_especial

    def extrato(self):
        print(f'Número da conta: {self.numero}')
        print(f'Titular da conta: {self.nome}')
        print(f'Limite do Cheque Especial: {self.limite_cheque_especial}')


class ContaPoupanca(Conta):
    def __init__(self, numero, nome, saldo, rendimento, ):
        super().__init__(numero, nome, saldo)
        self.rendimento = rendimento

    def calcular_taxa_rendimento_mensal(self):
        saldo_atual = self.saldo
        saldo_atual = saldo_atual + (saldo_atual * (self.rendimento / 100))
        print(f'O saldo após o rendimento é de R$ {self.saldo}')


poupanca = ContaPoupanca('3248-X', 'Elvis', 2000, 1000.00)
print('Conta Poupança - Cliente:', poupanca.nome)
poupanca.calcular_taxa_rendimento_mensal()

corrente = ContaCorrente('5748-X', 'Elvis', 3000.00)
print('Conta Corrente - Cliente:', corrente.nome)
print('Limite Cheque Especial: ', corrente.limite_cheque_especial)
corrente.extrato()


class Veiculo:
    def __init__(self, marca: str, modelo: str, velocidadeMax: float, velocidadeAtual: float, ligado: bool, capacidade: int, tanque: float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.velocidadeMax = velocidadeMax
        self.velocidadeAtual = velocidadeAtual
        self.ligado = ligado
        self.capacidade = capacidade
        self.tanque = tanque

    def ligar(self):
        if self.ligado:
            print('O veículo já está ligado!')
        else:
            self.ligado = True
            print("O veículo está ligado")

    def desligar(self):
        if self.ligado == False:
            print('O veículo já está desligado!')
        else:
            self.ligado = False
            print("O veículo está desligado")

    def acelerar(self, velocidade):
        if self.ligado:
            if self.velocidadeAtual + velocidade < self.velocidadeMax:
                self.velocidadeAtual += velocidade
                print(f'A velocidade atual do veículo depois de acelerar é {self.velocidadeAtual}')
            else:
                print('Você já chegou na velocidade máxima do veículo')

    def frear(self, percentual):
        if self.velocidadeAtual - (self.velocidadeAtual * (percentual / 100)) >= 0:
            self.velocidadeAtual -= (self.velocidadeAtual * (percentual / 100))
            print(f'A velocidade do veículo foi reduzida para {self.velocidadeAtual}')
        else:
            print('O carro já não pode frear porque está parado.')

    def exibirDados(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Velocidade Máxima: {self.velocidadeMax}')
        print(f'Velocidade: {self.velocidadeAtual}')
        print(f'Ligado: {self.ligado}')
        print(f'Capacidade: {self.capacidade}')
        print(f'Tanque: {self.tanque}')


class Carro(Veiculo):
    def __init__(self, marca, modelo, velocidadeMax, velocidadeAtual, ligado, capacidade, tanque, quantidade_portas: int, abs: bool):
        super().__init__(marca, modelo, velocidadeMax, velocidadeAtual, ligado, capacidade, tanque)
        self.quantidade_portas = quantidade_portas
        self.abs = abs

    def darARe(self, velocidade):
        if self.velocidadeAtual - velocidade > -60 and self.velocidadeAtual == 0:
            self.velocidadeAtual -= velocidade
            print(f'A velocidade da marcha ré do carro é {self.velocidadeAtual}')
        else:
            print("Você atingiu a velocidade máxima da ré que é 60 km/h")

    def exibirDadosCarro(self):
        super().exibirDados()
        print(f'Quantidade de Portas: {self.quantidade_portas}')
        print(f'Abs: {self.abs}')


class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, velocidadeMax: float, velocidadeAtual: float, ligado: bool, capacidade: int, tanque: float, cilindradas: int) -> None:
        super().__init__(marca, modelo, velocidadeMax, velocidadeAtual, ligado, capacidade, tanque)
        self.cilindradas = cilindradas

    def exibirDadosMoto(self):
        super().exibirDados()
        print(f'Cilindradas: {self.cilindradas}')


carro = Carro('Chevrolet', 'Onix', 180.0, 0.0, False, 5, 50.0, 4, True)
moto = Moto('Honda', 'XRE', 160.0, 0.0, False, 2, 18.0, 300)

carro.ligar()
carro.acelerar(100)
print('---------------------')
moto.ligar()
moto.acelerar(60)
print('---------------------')
carro.frear(10)
print('---------------------')
moto.frear(10)
print('---------------------')

carro.exibirDadosCarro()
print('---------------------')
moto.exibirDadosMoto()

print('---------------------')
carro.desligar()
print('---------------------')
moto.desligar()















