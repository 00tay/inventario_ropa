from modelos.db import get_connection, get_db_path, init_db

def test_get_db_path():
    path = get_db_path()
    assert path.endswith("inventory.db")

def test_get_connection():
    with get_connection() as connection:
        assert connection is not None

def test_init_db():
    with get_connection() as connection:
       cursor =  connection.cursor()
       cursor.execute("SELECT name FROM sqlite_schema WHERE  type = 'table';")
       tables = cursor.fetchall()
       assert ("productos",) in tables
       assert ("variantes",) in tables