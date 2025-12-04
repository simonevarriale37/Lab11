from database.DB_connect import DBConnect


class DAO:
    """
        Implementare tutte le funzioni necessarie a interrogare il database.
        """

    @staticmethod
    def rifugi_per_anno(year : int):
        connessione = DBConnect.get_connection()
        cursor = connessione.cursor(dictionary=True)
        query = """SELECT c.id, c.id_rifugio1, c.id_rifugio2, 
                    r1.nome AS nome1, r1.localita AS localita1, 
                    r2.nome AS nome2, r2.localita AS localita2,
                    c.anno
                    FROM connessione c
                    JOIN rifugio r1 ON r1.id = c.id_rifugio1
                    JOIN rifugio r2 ON r2.id = c.id_rifugio2
                    WHERE c.anno <= %s
        """
        cursor.execute(query, (year,))
        risultato = cursor.fetchall()
        cursor.close()
        connessione.close()
        return risultato


