import sqlite3

class BD:
    def __init__(self):
        connect = sqlite3.connect("password.db")
        cursor = connect.cursor()
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS password (
                id INTEGER PRIMARY KEY,
                platform TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL      
            )         
            """
        )
        
        connect.commit()
        connect.close()

    def insert_bd(self, platfor : str, username : str, password : str):
        connect = sqlite3.connect("password.db")
        cursor = connect.cursor()
        
        cursor.execute("INSERT INTO password (platform, username, password) VALUES(?, ?, ?)",
            (platfor, username, password)
            )
        
        connect.commit()
        connect.close()
        
    def all_table(self):
        connect = sqlite3.connect("password.db")
        cursor = connect.cursor()
        
        cursor.execute("SELECT * FROM password")
        data = cursor.fetchall()
        
        connect.close()
        
        return data
    
    
tt = BD()
print(tt.all_table())