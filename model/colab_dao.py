from model.colab import Colab

def lista_colabAll():

    lista_colab = []
    for c in range(10):
        lista_colab.append(Colab("Colaborador "+str(c), "Descrição "+str(c), []))
    return lista_colab