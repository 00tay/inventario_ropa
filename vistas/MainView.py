import tkinter as tk
from PIL import Image, ImageTk

class MainView():
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario de Productos")
        self.centrar_pantalla()
        self.create_widgets()
        self.load_productos()

    def centrar_pantalla(self):
        width = 800
        height = 600
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_pos = (screen_width - width) // 2
        y_pos = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")

    def create_widgets(self):
        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.frame_lista = tk.Frame(self.container)
        self.frame_lista.pack(pady=40, fill="both", expand=True)

        search_frame = tk.Frame(self.frame_lista)
        search_frame.pack(pady=5)

        tk.Label(search_frame, text="Productos").pack(side="left")
        self.entry_search = tk.Entry(search_frame)
        self.entry_search.pack(side="left", padx=5)
        image = Image.open("./assets/lupa.png").resize((50, 50))
        image_tk   = ImageTk.PhotoImage(image)
        button = tk.Button(search_frame, text="Buscar",image=image_tk, compound="right" command=self.buscar_productos)
        button.pack(side="left")

    def load_productos(self):
        pass

    def buscar_productos(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()