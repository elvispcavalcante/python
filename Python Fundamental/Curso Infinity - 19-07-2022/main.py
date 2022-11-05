from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from projeto.CadAluno import Ui_CadAlunos
import conexao as conexao


class Banco:
    def __init__(self):
        self.conexao = conexao.Conexao()

    def listarAlunos(self):
        sql = "SELECT * FROM alunos"
        resultado = self.conexao.executarSql(sql)
        return resultado

    def buscarNome(self, nome):
        sql = "SELECT * FROM alunos WHERE nome LIKE %s"
        parametro = (f"%{nome}%")  # tupla
        resultado = self.conexao.executarSql(sql, parametro)
        return resultado

    def cadastrarAluno(self, nome, idade, curso):
        sql = "INSERT INTO alunos (nome, idade, curso) VALUES (%s, %s, %s)"
        parametro = (nome, idade, curso)  # tupla
        self.conexao.executarSql(sql, parametro, 'ins')

    def excluirAluno(self, matricula):
        sql = "DELETE FROM alunos WHERE matricula = %s"
        parametro = (matricula)  # tupla
        self.conexao.executarSql(sql, parametro, "del")

    def editarAluno(self, matricula, nome, idade, curso):
        sql = "UPDATE alunos SET Nome = %s, Idade = %s, Curso = %s WHERE Matricula = %s"
        parametro = (nome, idade, curso, matricula)
        self.conexao.executarSql(sql, parametro, 'upd')


class Janela(QMainWindow, Ui_CadAlunos):
    def __init__(self):
        super().__init__()
        self.db = Banco()
        self.setupUi(self)

        self.carregarTabela()

        self.btn_novo.clicked.connect(self.inserir)

        self.tb_alunos.cellClicked.connect(self.tabelaclique)
        self.btn_editar.clicked.connect(self.editar)
        self.btn_excluir.clicked.connect(self.excluir)
        self.txt_buscar.textChanged.connect(self.carregarTabela)

        self.btn_editar.setEnabled(False)
        self.btn_excluir.setEnabled(False)

    def carregarTabela(self):
        if self.txt_buscar.text() != "":
            nome = self.txt_buscar.text()
            resultado = self.db.buscarNome(nome)
        else:
            resultado = self.db.listarAlunos()

        self.tb_alunos.setRowCount(len(resultado))
        linha = 0
        for aluno in resultado:
            self.tb_alunos.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(aluno['matricula'])))
            self.tb_alunos.setItem(linha, 1, QtWidgets.QTableWidgetItem(aluno['nome']))
            self.tb_alunos.setItem(linha, 2, QtWidgets.QTableWidgetItem(str(aluno['idade'])))
            self.tb_alunos.setItem(linha, 3, QtWidgets.QTableWidgetItem(aluno['curso']))
            linha += 1

    def limparCampos(self):
        self.txt_matricula.setText("")
        self.txt_nome.setText("")
        self.txt_idade.setText("")
        self.cb_curso.setCurrentIndex(0)
        self.carregarTabela()

    def inserir(self):
        nome = self.txt_nome.text()
        idade = int(self.txt_idade.text())
        curso = self.cb_curso.currentText()
        self.db.cadastrarAluno(nome, idade, curso)
        QMessageBox.information(self, 'Cadastro', 'Aluno cadastrado com sucesso!!')
        self.limparCampos()

    def tabelaclique(self, row):
        matricula = self.tb_alunos.item(row, 0).text()
        nome = self.tb_alunos.item(row, 1).text()
        idade = self.tb_alunos.item(row, 2).text()
        curso = self.tb_alunos.item(row,3).text()

        self.txt_matricula.setText(matricula)
        self.txt_nome.setText(nome)
        self.txt_idade.setText(idade)
        self.cb_curso.setCurrentText(curso)

        self.btn_editar.setEnabled(True)
        self.btn_excluir.setEnabled(True)

    def editar(self):
        matricula = int(self.txt_matricula.text())
        nome = self.txt_nome.text()
        idade = int(self.txt_idade.text())
        curso = self.cb_curso.currentText()

        res = QMessageBox.question(self, "Tem certeza?", f"Deseja editar o aluno: {matricula}", QMessageBox.Yes | QMessageBox.No)

        if res == QMessageBox.Yes:
            self.db.editarAluno(matricula, nome, idade, curso)
            QMessageBox.information(self, "Edição", "Aluno alterado com sucesso!!")
            self.limparCampos()

    def excluir(self):
        matricula = self.txt_matricula.text()
        res = QMessageBox.question(self, "Tem certeza?", f"Deseja excluir o aluno: {matricula}",
                                   QMessageBox.Yes | QMessageBox.No)

        if res == QMessageBox.Yes:
            self.db.excluirAluno(matricula)
            QMessageBox.information(self, "Exclusão", "Aluno excluído com sucesso!!")
            self.limparCampos()



app = QApplication([])
window = Janela()
window.show()
app.exec()
