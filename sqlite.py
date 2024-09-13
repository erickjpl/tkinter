import sqlite3


class Database:
    name = "database.db"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create(self):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(75) NOT NULL
        )""")
        connect.commit()
        connect.close()

    def consultas(self, query, parameters=()):
        connect = sqlite3.connect(self.name)
        cursor = connect.cursor()
        result = cursor.execute(query, parameters)
        connect.commit()
        return result
    
    @staticmethod
    def query(query, parameters=()):
        try:
            with sqlite3.connect(Database.name) as connection:
                cursor = connection.cursor()
                cursor.execute(query, parameters)
                connection.commit()
                return cursor
        except sqlite3.Error as error:
            print(f"Database error: {error}")
            return None
    
    
