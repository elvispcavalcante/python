#Exercício 01 e 02
class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario
        self.horas_estagiadas = 0

class Estagiario(Funcionario):
    def __init__(self, matricula, nome, salario,):
        super().__init__(matricula, nome, salario)
        self.horas_estagiadas = 0

    def contratacao(self, horas):
        if self.horas_estagiadas + horas > 300:
            self.horas_estagiadas += horas
            print(f'Você será contratado porque já estagiou {self.horas_estagiadas} horas')
        else:
            print(f'O estágio ainda não acabou')

class Gerente(Funcionario):
    def __init__(self, matricula, nome, salario, setor, comissao):
        super().__init__(matricula, nome, salario)
        self.setor = setor
        self.comissao = comissao
        self.qtde_funcionarios = 0

    def contratar(self, quantidade):
        if quantidade < 10 and self.qtde_funcionarios < 10:
            self.qtde_funcionarios += quantidade
            print(f'Serão contratados {quantidade} funcionários')
        else:
            print(f'O setor já possui tem gente suficiente')


funcionario = Funcionario('321', 'Elvis', 3500.00)
print(funcionario.nome)
print(funcionario.matricula)
print(funcionario.salario)

estagiario = Estagiario('123', 'Leandro', 600.00)
print(estagiario.nome)
print(estagiario.matricula)
print(estagiario.salario)
estagiario.contratacao(400)

gerente = Gerente('456', 'Daniel', 3500.00, 'Financeiro', 500.00)
print(gerente.nome)
print(gerente.matricula)
print(gerente.salario)
print(gerente.setor)
print(gerente.comissao)
gerente.contratar(10)

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

