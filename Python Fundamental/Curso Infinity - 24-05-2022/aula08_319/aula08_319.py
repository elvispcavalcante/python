# class Elevador:
#     def __init__(self, andar_atual, capacidade, qtde_pessoas, qtde_andares):
#         self.qtde_andares = qtde_andares
#         self.andar_atual = andar_atual
#         self.capacidade = capacidade
#         self.qtde_pessoas = qtde_pessoas
#
#     def subir(self):
#         if self.andar_atual < self.qtde_andares:
#             self.andar_atual += 1
#             print(f"Você está no andar {self.andar_atual}")
#         else:
#             print("Não é possível subir pois você está no último andar")
#
#     def descer(self):
#         if self.andar_atual == 0:
#             print("Não é possível descer pois você está no terreo")
#         else:
#             self.andar_atual -= 1
#             print(f"Você está no andar {self.andar_atual}")
#
#     def entrar(self, quantidade_pessoas):
#         if quantidade_pessoas < self.capacidade and self.qtde_pessoas + quantidade_pessoas <= self.capacidade:
#             self.qtde_pessoas += quantidade_pessoas
#             print(f"O elevador está com {self.qtde_pessoas} pessoas")
#         else:
#             print("A quantidade de pessoas é maior do que a capacidade permitida!")
#
#     def sair(self, quantidade_pessoas):
#         if quantidade_pessoas <= self.qtde_pessoas and self.qtde_pessoas - quantidade_pessoas >= 0:
#             self.qtde_pessoas -= quantidade_pessoas
#             print(f"O elevador está com {self.qtde_pessoas} pessoas")
#         else:
#             print("A quantidade de pessoas a sair é maior do que quantidade de pessoas no elevador")
#
#
# elevador = Elevador(0, 6, 0, 6)
#
# elevador.subir()
# elevador.subir()
# elevador.subir()
# elevador.subir()
# elevador.subir()
# elevador.subir()
# elevador.descer()
# elevador.descer()
# elevador.descer()
# elevador.descer()
# elevador.descer()
# elevador.descer()
# elevador.descer()
# elevador.entrar(3)
# elevador.entrar(3)
# elevador.entrar(1)
# elevador.sair(3)
# elevador.sair(4)
# elevador.sair(3)

# class Pessoa:
#     def __init__(self):
#         self.__nome = ''
#         self.__idade = 0
#         self.__cpf = ''
#
#     @property
#     def nome(self):
#         return self.__nome
#
#     @property
#     def idade(self):
#         return self.__idade
#
#     @property
#     def cpf(self):
#         return self.__cpf
#
#     @nome.setter
#     def nome(self, nome):
#         raise Exception("Não é possível atribuir o nome utilizando a função. Utilize a função setNome")
#
#     @idade.setter
#     def idade(self, idade):
#         self.__idade = idade
#
#     @cpf.setter
#     def cpf(self, cpf):
#         self.__cpf = cpf
#
#     def setNome(self, nome):
#         self.__nome = nome
#
#
# pessoa = Pessoa()
#
# pessoa.setNome("Elvis")
# pessoa.idade = 35
# pessoa.cpf = "111.111.111-11"
#
# print(pessoa.nome)
# print(pessoa.idade)
# print(pessoa.cpf)
#


class Biblioteca:
    def __init__(self):
        self.__nome = ''
        self.__capacidade_livros = 0
        self.__localizacao = ''
        self.__livros = []

    @property
    def nome(self):
        return self.__nome

    @property
    def capacidade_livros(self):
        return self.__capacidade_livros

    @property
    def localizacao(self):
        return self.__localizacao

    @property
    def livros(self):
        raise Exception("Utilize o método exibir_livros")

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @capacidade_livros.setter
    def capacidade_livros(self, capacidade):
        self.__capacidade_livros = capacidade

    @localizacao.setter
    def localizacao(self, localizacao):
        self.__localizacao = localizacao

    @livros.setter
    def livros(self, livro):
        raise Exception("Utilize o método adicionar_livros")

    def adicionar_livro(self, nome_livro:str):
        if len(self.__livros) < self.capacidade_livros:
            self.__livros.append(nome_livro)
        else:
            print(f"Não é possível adicionar o livro {nome_livro} pois a capacidade foi ultrapassada!")

    def exibir_livros(self):
        print(f"Os livros que fazem parte da {self.__nome}: ")
        for livro in self.__livros:
            print(f"Livro: {livro}")


biblioteca = Biblioteca()

biblioteca.nome = 'Biblioteca Infinity'
biblioteca.capacidade_livros = 5
biblioteca.localizacao = 'Avenida Santos Dumont, Aldeota'
#biblioteca.livros = "teste"

biblioteca.adicionar_livro("Scrum")
biblioteca.adicionar_livro("HTML/CSS")
biblioteca.adicionar_livro("Java Use a Cabeça")
biblioteca.adicionar_livro("Banco de Dados")
biblioteca.adicionar_livro("Python")
biblioteca.adicionar_livro("C#")

#print(biblioteca.livros())
biblioteca.exibir_livros()

