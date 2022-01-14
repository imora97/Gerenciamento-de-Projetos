
from qt_core import *


class CardProjeto(QWidget):

    def __init__(self, projeto):
        super().__init__()
        uic.loadUi('view/card_projeto.ui', self)

        self.projeto = projeto
        
        self.nome_do_projeto.setText(projeto.nome)

        self.abrir_button.clicked.connect(self.abreprojeto)

    def abreprojeto(self):
        print('Abra o projeto ', self. projeto.nome)