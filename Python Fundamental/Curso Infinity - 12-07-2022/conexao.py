import pymysql.cursors


# conexao = pymysql.connect(host='localhost',
#                           user='root',
#                           password='admin',
#                           database='escola',
#                           cursorclass=pymysql.cursors.DictCursor)

# cursor = conexao.cursor()
# sql = 'SELECT * FROM alunos'
# cursor.execute(sql)
#
# resultado = cursor.fetchall()
#
# print(resultado)
# print(resultado[0]['matricula'])
# print(resultado[0]['nome'])
#
# print(resultado[1]['matricula'])
# print(resultado[1]['nome'])
#
# # noinspection PyUnresolvedReferences
# print(resultado[0].keys())
#
# for aluno in resultado:
#     print(aluno['nome'])
#
# cursor.close()
# conexao.close()


# with conexao.cursor() as cursor:
#     sql = 'SELECT * FROM alunos'
#     cursor.execute(sql)
#     resultado = cursor.fetchall()
#     for aluno in resultado:
#         print(aluno['nome'])

# with conexao.cursor() as cursor:
#     try:
#         sql = 'INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)'
#         dados_aluno = ('João', 20, 'Dev Full Stack')
#         cursor.execute(sql, dados_aluno)
#         conexao.commit()
#     except pymysql.err.ProgrammingError:
#         print("Erro encontrado no sql")

# with conexao.cursor() as cursor:
#     alunos = [('Hernande', 21, 'Fotografia'), ('Mayara', 23, 'Metaverso')]
#     sql = 'INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)'
#     cursor.executemany(sql, alunos)
#     conexao.commit()

# nome = input('Digite o novo nome: ')
# idade = int(input('Digite a nova idade: '))
# curso = input("Digite o novo Curso: ")
# matricula = int(input('Digite a matrícula: '))
#
# with conexao.cursor() as cursor:
#     sql = 'UPDATE alunos SET nome = %s, idade = %s, curso = %s WHERE matricula = %s'
#     cursor.execute(sql, (nome, idade, curso, matricula))
#     conexao.commit()

# matricula = tuple(input('Digite a matrícula para excluir: '))
#
# with conexao.cursor() as cursor:
#     sql = 'DELETE FROM alunos WHERE matricula = %s'
#     cursor.execute(sql, matricula)
#     conexao.commit()


class AlunoDao:
    def __init__(self):
        self.conexao = pymysql.connect(host='localhost',
                                  user='root',
                                  password='admin',
                                  database='escola',
                                  cursorclass=pymysql.cursors.DictCursor)

    def listarAlunos(self):
        with self.conexao.cursor() as cursor:
            sql = 'SELECT * FROM alunos'
            cursor.execute(sql)
            resultado = cursor.fetchall()

            for aluno in resultado:
                #print(aluno)
                print('Matricula: ', aluno["matricula"])
                print('Nome: ', aluno["nome"])
                print('Idade: ', aluno["idade"])
                print('Cursor: ', aluno["curso"])
                print('\n')

    def inserirAluno(self, aluno):
        with self.conexao.cursor() as cursor:
            try:
                sql = 'INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)'
                dados_aluno = (aluno.nome, aluno.idade, aluno.curso)
                cursor.execute(sql, dados_aluno)
                self.conexao.commit()
            except pymysql.err.ProgrammingError:
                print("Erro encontrado no sql")

    def atualizarAluno(self, aluno):
        with self.conexao.cursor() as cursor:
            sql = 'UPDATE alunos SET nome = %s, idade = %s, curso = %s WHERE matricula = %s'
            cursor.execute(sql, (aluno.nome, aluno.idade, aluno.curso, aluno.matricula))
            self.conexao.commit()

    def apagarAluno(self, matricula):
        with self.conexao.cursor() as cursor:
            sql = 'DELETE FROM alunos WHERE matricula = %s'
            cursor.execute(sql, matricula)
            self.conexao.commit()


class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso


aluno = Aluno('Wesley', 20, 'Fotografia')

al = AlunoDao()
al.listarAlunos()
# al.inserirAluno(aluno)
al.apagarAluno(6)


