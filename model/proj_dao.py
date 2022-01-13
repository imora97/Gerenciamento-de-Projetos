from model.projet import Projeto

def listaAll():
    
    lista = []
    for i in range(10):
        lista.append(Projeto("Projeto "+str(i), "Descrição "+str(i), []))
    return lista