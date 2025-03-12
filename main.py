from tkinter import Tk
from vistas.MainView import MainView

if __name__ == '__main__':
    root = Tk()
    app = MainView(root)
    root.mainloop()