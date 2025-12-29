import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.dao = DAO()
        self.lista_classificazioni = self.dao.estrai_classificazione()
        self.lista_geni = self.dao.estrai_gene()
        self.lista_interazioni = self.dao.estrai_interazione()
        self.G = nx.DiGraph()
        self.dizionario_geni = {}
        for i in self.lista_geni:
            self.dizionario_geni[i.id]= i.cromosoma



    def crea_grafo(self):
        for i in self.lista_geni:
            cromosoma = i.cromosoma
            if int(cromosoma) == 0:
                continue
            else:
                self.G.add_node(cromosoma)
        lista = []
        for i in self.lista_interazioni:
            id1 = i.id_gene1
            id2 = i.id_gene2
            correlazione = float(i.correlazione)


            if (id1,id2) not in lista or (id2,id1) not in lista:  ##elimino i duplicati
                lista.append((id1,id2,correlazione))
        for i in lista:
            id1 = i[0]
            id2 = i[1]
            correlazione = i[2]
            try:
                cromosoma1= self.dizionario_geni[id1]
                cromosoma2= self.dizionario_geni[id2]
            except KeyError:
                continue
            if cromosoma1 != cromosoma2:
                if self.G.has_edge(cromosoma1,cromosoma2):
                    self.G[cromosoma1][cromosoma2]['weight'] = self.G[cromosoma1][cromosoma2]['weight']+correlazione

                else:
                    self.G.add_edge(cromosoma1,cromosoma2,weight = correlazione)

    def ricorsione(self,primo,lista_parziali, lista, soglia,costo,costo_massimo):

        if len(lista_parziali)==0:
            lista_parziali.append(primo)

        vicini = list(self.G.neighbors(primo))
        esteso = False

        for j in vicini:
            if j in lista_parziali:
                continue
            costo1 = self.G[primo][j]['weight']
            if costo1 <= soglia:
                continue
            lista_parziali.append(j)

            nuovo_costo = costo + costo1

            esteso = True
            self.ricorsione(j, lista_parziali, lista, soglia, nuovo_costo, costo_massimo)

            lista_parziali.pop()

        if not esteso:
            if costo>costo_massimo[0]:
                lista.clear()
                lista.append([lista_parziali.copy(), costo])
                costo_massimo[0]= costo




    def ricerca_ricorsiva(self, soglia):
        lista_totali = []
        for i in self.G.nodes():
            print(i)
            lista_parziali = []
            lista = []
            costo = 0
            costo_massimo = [0]
            self.ricorsione(i, lista_parziali, lista, int(soglia), costo, costo_massimo)
            if lista:
                if len(lista_totali)==0:
                    lista_totali.append((lista[0][0],lista[0][1]))
                else:
                    if lista[0][1]>lista_totali[0][1]:
                        lista_totali.clear()
                        lista_totali.append((lista[0][0],lista[0][1]))
                    else:
                        pass

        return lista_totali

















