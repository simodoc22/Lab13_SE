from database.DB_connect import DBConnect  ##15.46
from model.classificazione import Classificazione
from model.interazione import Interazione
from model.gene import Gene
class DAO:

    @staticmethod
    def estrai_classificazione():
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM classificazione """
        cursor.execute(query)
        result = []
        for row in cursor:
            oggetto = Classificazione(row['id_gene'], row['localizzazione'])
            result.append(oggetto)


        cursor.close()
        conn.close()
        return result

    @staticmethod
    def estrai_interazione():
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM interazione """
        cursor.execute(query)
        result = []
        for row in cursor:
            oggetto = Interazione(row['id_gene1'], row['id_gene2'],row["tipo"],row["correlazione"])
            result.append(oggetto)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def estrai_gene():
        conn = DBConnect.get_connection()

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM gene """
        cursor.execute(query)
        result = []
        for row in cursor:
            oggetto = Gene(row['id'], row['funzione'],row["essenziale"],row["cromosoma"])
            result.append(oggetto)
        cursor.close()
        conn.close()
        return result
