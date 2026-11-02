import mysql.connector


class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self.nome = nome
        self.responsabile = responsabile

    @staticmethod
    def get_db_connection():
        # Parametri standard di XAMPP richiesti dalla traccia
        return mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="deposito_strumenti"
        )

    def get_tutti_strumenti(self):
        cnx = self.get_db_connection()
        cursor = cnx.cursor(dictionary=True)
        cursor.execute("SELECT * FROM strumento")

        # fetchall() restituisce una lista, risolvendo il warning di PyCharm
        strumenti = [
            f"[{row['id']}] {row['nome']} - Tipo: {row['tipo']}"
            for row in cursor.fetchall()
        ]

        cursor.close()
        cnx.close()
        return strumenti

    def cerca_per_tipo(self, tipo):
        cnx = self.get_db_connection()
        cursor = cnx.cursor(dictionary=True)

        query = "SELECT * FROM strumento WHERE tipo = %s"
        cursor.execute(query, (tipo,))

        strumenti = [
            f"[{row['id']}] {row['nome']} - Tipo: {row['tipo']}"
            for row in cursor.fetchall()
        ]

        cursor.close()
        cnx.close()
        return strumenti