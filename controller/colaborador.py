from qt_core import *

class Colaborador(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('view/colaborador.ui', self)
