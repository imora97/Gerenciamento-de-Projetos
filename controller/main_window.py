from controller.lista_de_projetos import ListadeProjetos
from controller.nv_projeto import NovoProjeto
from controller.colaborador import Colaborador
from qt_core import *

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        # define página inicial
        self.stackedWidget.insertWidget(0, ListadeProjetos())

        # define ações dos botões
        self.lista_proj_button.clicked.connect(self.abrelista)
        self.nv_proj_button.clicked.connect(self.abrenovoprojeto)
        self.colab_button.clicked.connect(self.abrecolaborador)

    def abrelista(self):
        self.stackedWidget.insertWidget(0, ListadeProjetos())
        self.stackedWidget.setCurrentIndex(0)

    def abrenovoprojeto(self):
        self.stackedWidget.insertWidget(0, NovoProjeto())
        self.stackedWidget.setCurrentIndex(0)

    def abrecolaborador(self):
        self.stackedWidget.insertWidget(0, Colaborador())
        self.stackedWidget.setCurrentIndex(0)
