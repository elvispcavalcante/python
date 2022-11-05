from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from template import Ui_MainWindow
from pygui import JanelaTeste


class Janela(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.cadastrar)

    def cadastrar(self):
        text = self.cb_graduacao.currentText()
        print(text)

        if self.ck_manha.isChecked() and self.ck_tarde.isChecked():
            QMessageBox.information(self, 'Informação', 'Você selecionou os turnos Manhã e Tarde')
        elif self.ck_manha.isChecked() and self.ck_noite.isChecked():
            QMessageBox.information(self, 'Informação', 'Você selecionou os turnos Manhã e Noite')
        elif self.ck_tarde.isChecked() and self.ck_noite.isChecked():
            QMessageBox.information(self, 'Informação', 'Você selecionou os turnos Tarde e Noite')
        else:
            QMessageBox.critical(self, 'Erro', 'Você precisa selecionar pelo menos dois turnos')

        self.janela3 = JanelaTeste()
        self.janela3.show()

app = QApplication([])
window = Janela()
window.show()
app.exec_()

