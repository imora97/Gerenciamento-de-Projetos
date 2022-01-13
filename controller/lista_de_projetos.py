from controller.card_projeto import CardProjeto
from qt_core import *
import model.proj_dao as ProjetoDAO
from controller.card_projeto import CardProjeto

class ListadeProjetos(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('view/lista_de_projetos.ui', self)

        self.lista = ProjetoDAO.listaAll()

        for projeto in self.lista:
           self.add_card(projeto)

    def add_card(self, projeto):
        self.painel_proj.addWidget(CardProjeto(projeto))