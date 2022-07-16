"""
- Áries: de 21 março a 20 abril;
- Touro: de 21 abril a 20 maio;
- Gêmeos: de 21 maio a 20 junho;
- Câncer: de 21 junho a 22 julho;
- Leão: de 23 julho a 22 agosto;
- Virgem: de 23 agosto a 22 setembro;
- Libra: de 23 setembro a 22 outubro;
- Escorpião: de 23 outubro a 21 novembro;
- Sagitário: de 22 novembro a 21 dezembro;
- Capricórnio: de 22 dezembro a 20 janeiro;
- Aquário: de 21 janeiro a 18 fevereiro;
- Peixes: de 19 fevereiro a 20 março.
"""
#Mostrar qual o signo

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))

if mes == 3:
    if dia >= 1 and dia <= 20:
        print("O seu signo é Peixes")
    elif dia >= 21 and dia <= 31:
        print("O seu signo é Áries")
elif mes == 4:
    if dia >= 1 and dia <= 20:
        print("O seu signo é Áries")
    elif dia >=21 and dia <= 30:
        print("O seu signo é Touro")
elif mes == 5:
    if dia >= 1 and dia <= 20:
        print("O seu signo é Touro")
    elif dia >= 21 and dia <= 31:
        print("O seu signo é Gêmeos")
elif mes == 6:
    if dia >= 1 and dia <= 20:
        print("O seu signo é Gêmeos")
    elif dia >= 21 and dia <= 30:
        print("O seu signo é Câncer")
elif mes == 7:
    if dia >= 1 and dia <= 22:
        print("O seu signo é Câncer")
    elif dia >= 23 and dia <= 31:
        print("O seu signo é Leão")
elif mes == 8:
    if dia >= 1 and dia <= 22:
        print("O seu signo é Leão")
    elif dia >= 23 and dia <= 31:
        print("O seu signo é Virgem")
elif mes == 9:
    if dia >= 1 and dia <= 22:
        print("O seu signo é Virgem")
    elif dia >= 23 and dia <= 30:
        print("O seu signo é Libra")
elif mes == 10:
    if dia >= 1 and dia <= 22:
        print("O seu signo é Libra")
    elif dia >= 23 and dia <= 31:
        print("O seu signo é Escorpião")
elif mes == 11:
    if dia >= 1 and dia <= 21:
        print("O seu signo é Escorpião")
    elif dia >= 22 and dia <= 30:
        print("O seu signo é Sagitário")
elif mes == 12:
    if dia >= 1 and dia <= 21:
        print("O seu signo é Sagitário")
    elif dia >= 22 and dia <= 31:
        print("O seu signo é Capricórnio")
elif mes == 1:
    if dia >= 1 and dia <= 20:
        print("O seu signo é Capricórnio")
    elif dia >= 21 and dia <= 31:
        print("O seu signo é Aquário")
elif mes == 2:
    if dia >= 1 and dia <= 18:
        print("O seu signo é Aquário")
    elif dia >= 19 and dia <= 29:
        print("O seu signo é Peixes")
