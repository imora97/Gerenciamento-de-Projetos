from qt_core import *

class NovoProjeto(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('view/nv_projeto.ui', self)