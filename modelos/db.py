import sqlite3
import os
import logging
from logging.handlers import SysLogHandler

logging.basicConfig(filename="error_logs.log", filemode="w" , format="%(asctime)s %(message)s", level=logging.ERROR)

def get_db_path():

    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(base_dir,"..", "databases")

    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    db_name = 'inventory.db'
    db_path = os.path.join(db_dir, db_name)
    return os.path.abspath(db_path)

def get_connection():

    db_path = get_db_path()
    return sqlite3.connect(db_path)

def init_db():
    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("BEGIN")

            cursor.execute("""

                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    categoria TEXT,
                    precio REAL NOT NULL,
                    proveedor TEXT NOT NULL
                 )
                           
            """)

            cursor.execute("""
                        
                CREATE TABLE IF NOT EXISTS variantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    talla TEXT NOT NULL,
                    stock REAL,
                    color TEXT NOT NULL,
                    productos_id INTEGER,
                    FOREIGN KEY (productos_id) REFERENCES productos(id) ON DELETE CASCADE
                )
                
            """)

            connection.commit()
    
    except sqlite3.Error as e:
        connection.rollback()
        (logging.error(e))

if __name__ == '__main__':
    init_db()