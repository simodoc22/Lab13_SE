class Classificazione:
    def __init__(self,id_gene,localizzazione):
        self.id_gene = id_gene
        self.localizzazione = localizzazione
    def __str__(self):
        return str(self.id_gene)
    def __hash__(self):
        return hash(self.id_gene)