from tkinter import Tk
from modelos.db import init_db
from vistas.main_view import MainView

if __name__ == '__main__':
    init_db()
    root = Tk()
    app = MainView(root)
    root.mainloop()