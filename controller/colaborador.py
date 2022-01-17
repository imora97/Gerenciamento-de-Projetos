from qt_core import *
import model.colab_dao as ColabDAO
import model.colab as Colab

class Colaborador(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('view/colaborador.ui', self)

        # informações do colaborador
        self.nome_colab.setText(ColabDAO.nome)
        self.email_colab.setText(ColabDAO.email)

        # ações botões
        self.excluir_button.clicked.connect(self.exclui_colab)
        self.limpar_button.clicked.connect(self.limpa_campo)
        self.salvar_button.clicked.connect(self.salva_colab)

    def exclui_colab(self):
        self.tableWidget.insertWidget(0, Colaborador())
        self.tableWidget.setCurrentIndex(0)

    def limpa_campo(self):
        self.tableWidget.insertWidget(0, Colaborador())
        self.tableWidget.setCurrentIndex(0)

    def salva_colab(self):
        nome = self.nome.text()
        email = self. email.text()

        nv_colab = Colab(nome, email)

        ColabDAO.adicionar(nv_colab)
        
        self.tableWidget.insertWidget(0, Colaborador())
        self.tableWidget.setCurrentIndex(0)
