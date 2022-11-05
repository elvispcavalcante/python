class Funcionario:
    def __init__(self, nome, salario, matricula, funcao):
        self.__nome = nome
        self.__salario = salario
        self.__matricula = matricula
        self.__funcao = funcao

    @property
    def nome(self):
        return self.__nome

    @property
    def salario(self):
        return self.__salario

    @property
    def matricula(self):
        return self.__matricula

    @property
    def funcao(self):
        return self.__funcao

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @salario.setter
    def salario(self, salario):
        raise Exception("Não é possível alterar o valor por essa função!")

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao

    def reajustarSalario(self, percentualAumento):
        salario_reajustado = 0
        if percentualAumento > 0 and percentualAumento <= 20:
            salario_reajustado = self.__salario + ((self.__salario * percentualAumento)/100)
            self.__salario = salario_reajustado
        elif percentualAumento < 0:
            print("Não é possível diminuir o salário atual do funcionário")
        else:
            print("O percentual passado não pode ser utilizado para reajustar o salário")


func = Funcionario("Elvis", 10000, 12345, "Analista de TI")
#func.salario = 1000

func.reajustarSalario(10)
print(func.salario)