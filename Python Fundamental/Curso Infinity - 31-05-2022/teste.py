# class Tamagoshi:
#     def __init__(self, nome, idade=0, fome=0, saude=100):
#         self.__nome = nome
#         self.__fome = fome
#         self.__saude = saude
#         self.__idade = idade
#
#     @property
#     def nome(self):
#         return self.__nome
#
#     @property
#     def fome(self):
#         return self.__fome
#
#     @property
#     def saude(self):
#         return self.__saude
#
#     @property
#     def idade(self):
#         return self.__idade
#
#     @nome.setter
#     def nome(self, nomeAlterado):
#         self.__nome = nomeAlterado
#
#     @fome.setter
#     def fome(self, situacaoFome):
#         self.__fome = situacaoFome
#
#     @saude.setter
#     def saude(self, situacaoSaude):
#         self.__saude = situacaoSaude
#
#     @idade.setter
#     def idade(self, idadePassada):
#         self.__idade = idadePassada
#
#     def humor(self):
#         fome = self.__fome
#         saude = self.__saude
#
#         if 0 <= fome < 25 and 75 < saude <= 100:
#             return 'O bichinho está feliz'
#         elif 25 <= fome < 50 and 50 < saude <= 75:
#             return 'O bichinho está contente'
#         elif 50 <= fome < 75 and 25 < saude <= 50:
#             return 'O bichinho está triste'
#         elif 75 <= fome < 99 and 1 < saude <= 25:
#             return 'O bichinho está passando mal'
#         elif fome >= 100 and saude <= 0:
#             return 'O bichinho morreu'
#         else:
#             return 'O bichinho não está bem, veja o está acontecendo'
#
#
# tamagoshi = Tamagoshi('C')
#
# print('Nome:', tamagoshi.nome)
# print('Idade:', tamagoshi.idade)
# print('Saúde:', tamagoshi.saude)
# print('Fome:', tamagoshi.fome)
# humor = tamagoshi.humor()
# print('Humor:', humor)
#
# tamagoshi.idade = 2
# tamagoshi.fome = 55
# tamagoshi.saude = 40
#
# print('----------------------')
# print('Nome:', tamagoshi.nome)
# print('Idade:', tamagoshi.idade)
# print('Saúde:', tamagoshi.saude)
# print('Fome:', tamagoshi.fome)
# humor = tamagoshi.humor()
# print('Humor:', humor)
#


class Endereco:
    def __init__(self, bairro, cidade):
        self.bairro = bairro
        self.cidade = cidade


endereco1 = Endereco('Aldeota', 'Fortaleza')
endereco2 = Endereco('Centro', 'Fortaleza')
endereco3 = Endereco('Parquelândia', 'Fortaleza')
endereco4 = Endereco('Meireles', 'Fortaleza')

lista = [endereco1, endereco2, endereco3, endereco4]

for endereco in lista:
    print(f'Bairro: {endereco.bairro}, Cidade: {endereco.cidade}'.center(20))



