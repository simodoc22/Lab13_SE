class Gene:
    def __init__(self,id,funzione,essenziale,cromosoma):
        self.id = id
        self.funzione = funzione
        self.essenziale = essenziale
        self.cromosoma = cromosoma
    def __str__(self):
        return str(self.id)
    def __hash__(self):
        return hash(self.id)