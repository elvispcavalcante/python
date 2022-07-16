"""
idade -> até 2 anos = filhotes e acima de 2 anos = adultos
castrado -> sim ou não
sexo -> macho ou femea
FivFelv positivo (Aids do gato) -> sim ou não

gatos igual ou abaixo de 2 anos = filhotes
gatos acima de 2 anos = adultos

1ª situação: Ficam na Sala A - filhotes castrados, independentes de M ou F. Se for fêmea e não castrada fica na sala A. contanto
que não tenha FivFelv

2º situação: gatos acima de 2 anos, são adultos e ficam na sala B. Todos os adultos são castrados.

3º situação: gatos adultos não castrados ficam na sala C

4ª situação: ficam os gatos com FivFelv positivo com qualquer idade e todos machos.

5ª situação: Fêmeas com FivFelv não ficam nesse gatil, são direcionadas para outro gatil
"""

print("Antes de alocarmos os gatos nas salas de adoção precisamos conferir algumas informações: ")
while True:
    idade = int(input("Primeira, qual a idade do(a) gato(a)? "))
    castrado = input("Segunda, o(a) gato(a) é castrado(a)? Digite sim ou nao: ")
    sexo = input("Terceira, qual o gênero do animal? Digite macho ou femea: ")
    fivfelv = input("Quarta, o(a) gato(a) possui teste positivo para FivFelv? Digite sim ou nao: ")
    if idade <= 2 and fivfelv == 'nao':
        if sexo == 'femea':
            print("A gata ficará na sala A")
        else:
            print("O gato ficará na sala A")
    elif idade > 2 and castrado == 'sim' and fivfelv == 'nao':
        if sexo == 'femea':
            print("A gata ficará na sala B")
        else:
            print("O gato ficará na sala B")
    elif idade > 2 and castrado == 'nao' and fivfelv == 'nao':
        if sexo == 'femea':
            print("A gata ficará na sala C")
        else:
            print("O gato ficará na sala C")
    elif sexo == 'macho' and fivfelv == 'sim':
        print("O gato ficará na sala D")
    elif sexo == 'femea' and fivfelv == 'sim':
        print("A gata terá que ser alocada em outro gatil!")
    else:
        print("Verifique as informações prestadas, pois não foram corretamente digitadas de acordo com o que foi pedido")

    continuar = input("Deseja continuar a inserir informações? Digite sim ou nao: ")
    if continuar == "nao":
        break
    else:
        continue

