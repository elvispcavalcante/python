import pymysql.cursors

class professoresDao:

    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                       user='root',
                                       password='admin',
                                       database='escola',
                                       cursorclass=pymysql.cursors.DictCursor)

    def listarProfessores(self):
        with self.conexao.cursor() as cursor:
            sql = 'SELECT * FROM professores'
            cursor.execute(sql)
            resultado = cursor.fetchall()

            for professor in resultado:
                print(f"Matrícula: {professor['matricula']}")
                print(f"Nome: {professor['nome']}")
                print(f"Área: {professor['area']}")
                print(f"Salário: {professor['salario']}")


    def inserirProfessor(self, professor):
        with self.conexao.cursor() as cursor:
            sql = "INSERT INTO professores (nome, area, salario) VALUES (%s, %s, %s)"
            cursor.execute(sql, (professor.nome, professor.area, professor.salario))
            self.conexao.commit()

    def atualizarProfessor(self, professor):
        with self.conexao.cursor() as cursor:
            sql = "UPDATE professores SET nome = %s, area = %s, salario = %s WHERE matricula = %s"
            cursor.execute(sql, (professor.nome, professor.area, professor.salario, professor.matricula))
            self.conexao.commit()

    def deletarProfessor(self, matricula):
        with self.conexao.cursor() as cursor:
            sql = "DELETE FROM professores WHERE matricula = %s"
            cursor.execute(sql, matricula)
            self.conexao.commit()


class Professor:
    def __init__(self, nome, area, salario: float, matricula=None):
        self.matricula = matricula
        self.nome = nome
        self.area = area
        self.salario = salario

condicao = True

print("Seja bem-vindo ao sistema de professores da escola")

while condicao:
    print('O que deseja realizar agora? Cadastrar, Listar, Atualizar ou Deletar')
    opcao_escolhida = input('Digite C para Cadastrar, L para Listar, A para Atualizar, D para Deletar: ')

    if opcao_escolhida.lower() == 'l':
        professoresDao().listarProfessores()

        continua = input("Deseja continuarL? S ou N ")
        if continua.lower() == 's':
            pass
        else:
            condicao = False
            break
    elif opcao_escolhida.lower() == 'c':
        nome_professor = input("Digite o nome do professor: ")
        area_professor = input("Digite a área do professor: ")
        salario_professor = float(input("Digite o salário do professor: "))
        professor = Professor(nome_professor, area_professor, salario_professor)
        professoresDao().inserirProfessor(professor)
        continua = input("Deseja continuar? S ou N ")
        if continua.lower() == 's':
            print("\n")
        else:
            condicao = False
            break

    elif opcao_escolhida.lower() == 'a':
        nome_professor = input("Digite o nome do professor: ")
        area_professor = input("Digite a área do professor: ")
        salario_professor = float(input("Digite o salário do professor: "))
        matricula_professor = int(input("Digite a matrícula do professor: "))
        professor = Professor(nome_professor, area_professor, salario_professor, matricula_professor)
        professoresDao().atualizarProfessor(professor)

        continua = input("Deseja continuar? S ou N ")
        if continua.lower() == 's':
            print("\n")
        else:
            condicao = False
            break
    elif opcao_escolhida.lower() == 'd':
        matricula_professor = int(input("Digite a matrícula do professor: "))
        professoresDao().deletarProfessor(matricula_professor)

        continua = input("Deseja continuar? S ou N ")
        if continua.lower() == 's':
            print("\n")
        else:
            condicao = False
            break
    else:
        print('A opção digitada é inválida!')



# professoresDao().listarProfessores()
# professoresDao().inserirProfessor(professor)
# professoresDao().atualizarProfessor(professor)
# professoresDao().deletarProfessor(2)
