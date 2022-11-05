from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel
import random

class JanelaTeste(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.label.setText("Exemplo de Label:")
        self.label.move(50, 30)
        self.label.resize(150, 30)
        self.label.setStyleSheet('QLabel{font-weight: bold; font-size: 15px; border: 1px solid black}')

        self.campo = QLineEdit(self)
        self.campo.move(205, 30)
        self.campo.resize(200, 30)

        self.botao = QPushButton("Clique Aqui", self)
        self.botao.move(200, 300)
        self.botao.resize(200, 50)
        self.botao.clicked.connect(self.clicou)
        self.botao.setStyleSheet("QPushButton {background-color: #03fc90; "
                                 "border: 1px solid black; border-radius: 10px;} ")
        self.carregarJanela()

    def carregarJanela(self):
        self.setGeometry(650, 340, 600, 400)
        self.show()

    def clicou(self):
        # print('Você clicou no botão!')
        # v, am, az = self.mudarCorBotao()
        # # print(f'Cor Vermelha: {v}')
        # # print(f'Cor Amarela: {am}')
        # # print(f'Cor Azul: {az}')
        # texto = "QPushButton{background: rgb({v}, {am}, {az}); border: 1px solid black; border-radius: 10px;}"
        # texto = texto.replace("{v}", f"{v}").replace("{am}", f"{am}").replace("{az}", f"{az}")
        # # texto = texto.replace("{am}", f"{am}")
        # # texto = texto.replace("{az}", f"{az}")
        # # print(texto)
        # self.botao.setStyleSheet(texto)
        self.janela2 = JanelaOutra()
        # self.hide()

    def mudarCorBotao(self):
        vermelho = random.randint(0, 255)
        amarelo = random.randint(0, 255)
        azul = random.randint(0, 255)
        return vermelho, amarelo, azul


class JanelaOutra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Exemplo de Label:")
        self.label.move(50, 30)
        self.label.resize(150, 30)
        self.label.setStyleSheet('QLabel{font-weight: bold; font-size: 15px; border: 1px solid black}')

        self.campo = QLineEdit(self)
        self.campo.move(205, 30)
        self.campo.resize(200, 30)

        self.botao = QPushButton("Visualize o texto digitado", self)
        self.botao.move(200, 150)
        self.botao.resize(200, 50)
        self.botao.clicked.connect(self.clicou)
        self.botao.setStyleSheet("QPushButton {background-color: #03fc90; "
                                 "border: 1px solid black; border-radius: 10px;} ")
        self.carregarJanela()

    def carregarJanela(self):
        self.setGeometry(650, 340, 600, 400)
        self.show()

    def clicou(self):
        texto = self.campo.text()
        self.label.setText(texto)
        v, am, az = self.mudarCorBotao()
        # print(f'Cor Vermelha: {v}')
        # print(f'Cor Amarela: {am}')
        # print(f'Cor Azul: {az}')
        texto = "QPushButton{background: rgb({v}, {am}, {az}); border: 1px solid black; border-radius: 10px;}"
        texto = texto.replace("{v}", f"{v}").replace("{am}", f"{am}").replace("{az}", f"{az}")
        # texto = texto.replace("{am}", f"{am}")
        # texto = texto.replace("{az}", f"{az}")
        # print(texto)
        self.botao.setStyleSheet(texto)

    def mudarCorBotao(self):
        vermelho = random.randint(0, 255)
        amarelo = random.randint(0, 255)
        azul = random.randint(0, 255)
        return vermelho, amarelo, azul


# app = QApplication([])
# window = JanelaTeste()
# app.exec()
