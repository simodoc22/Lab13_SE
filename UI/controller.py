import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_graph(self, e):
        """ Handler per gestire creazione del grafo """""
        self._model.crea_grafo()
        numero_di_archi = self._model.G.number_of_edges()
        numero_nodi= self._model.G.number_of_nodes()
        massimo = ""
        for i,j in self._model.G.edges():
            if i != j:
                valore = self._model.G[i][j]["weight"]
                if massimo == "":
                    massimo = valore
                else:
                    if valore > massimo:
                        massimo = valore
                    else:
                        pass

        minimo = ""
        for i,j in self._model.G.edges():
            if i!=j:
                valore = self._model.G[i][j]["weight"]
                if minimo == "":
                    minimo = valore
                else:
                    if valore<minimo:
                        minimo = valore
                    else:
                        pass



        valore_minimo = minimo
        valore_massimo = massimo
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"numero di nodi : {numero_nodi}"))
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"numero di archi : {numero_di_archi}"))
        self._view.lista_visualizzazione_1.controls.append(ft.Text(f"informazioni sui pesi degli archi : valore_minimo {valore_minimo} valore massimo {valore_massimo}"))
        self._view.update()

    def handle_conta_edges(self, e):
        """ Handler per gestire il conteggio degli archi """""
        soglia = int(self._view.txt_name.value)
        if 2 <soglia<8:
            lista_maggiori = []
            lista_minori = []
            for i,j in self._model.G.edges():
                if self._model.G[i][j]["weight"] < soglia:
                    lista_minori.append((i,j))
                else:
                    if self._model.G[i][j]["weight"] > soglia:
                        lista_maggiori.append((i,j))
                    else:
                        pass
            numero1= len(lista_maggiori)
            numero2 = len(lista_minori)



            self._view.lista_visualizzazione_2.controls.append(ft.Text(f"archi con peso maggiore di soglia : {numero1}"))
            self._view.lista_visualizzazione_2.controls.append(ft.Text(f"archi con peso minore di soglia : {numero2}"))
            self._view.update()

        else:
            self._view.show_alert("attenzione inserire valore compreso tra 3 e 7 compresi")




    def handle_ricerca(self, e,):
        """ Handler per gestire il problema ricorsivo di ricerca del cammino """""
        lista_totali = self._model.ricerca_ricorsiva(self._view.txt_name.value)
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f"numero archi percorso massimo:{len(lista_totali[0][0])}"))
        self._view.lista_visualizzazione_3.controls.append(ft.Text(f"costo totale percorso massimo:{lista_totali[0][1]}"))
        for i in range(len(lista_totali[0][0])-1):
            primo_elemento=lista_totali[0][0][i]
            secondo_elemento=lista_totali[0][0][i+1]
            peso_tratto =self._model.G[primo_elemento][secondo_elemento]["weight"]
            self._view.lista_visualizzazione_3.controls.append(
                ft.Text(f"{primo_elemento}---->{secondo_elemento} peso: {peso_tratto}"))
        self._view.update()