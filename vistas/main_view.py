import tkinter as tk
from PIL import Image, ImageTk
from screeninfo import get_monitors
import vistas.product_form as product_form
from tkinter import messagebox
from controladores.producto_controlador import ProductoControlador

def get_monitor_info():
    monitors = get_monitors()
    return monitors[0].width

class MainView():
    def __init__(self, root):
        self.root = root
        self.root.title("Inventario de Productos")
        self.centrar_pantalla()
        self.create_widgets()
        self.load_productos("")

    def centrar_pantalla(self):
        width = 900
        height = 600
        screen_width = get_monitor_info()
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
        self.entry_search.bind("<Return>", lambda event: self.load_productos(self.entry_search.get().strip()))
        image = Image.open("./assets/lupa.png").resize((25, 25))
        self.image_tk   = ImageTk.PhotoImage(image)
        button = tk.Button(search_frame,image=self.image_tk, compound="right", command=lambda: self.load_productos(self.entry_search.get().strip()))
        button.pack(side="left")

        self.listbox_productos = tk.Listbox(self.frame_lista, width=82)
        self.listbox_productos.pack(padx=10, pady=10)
        # self.listbox_productos.bind("<Double-Button-1>", self.abrir_modificar_producto)

        frame_buttons = tk.Frame(self.frame_lista)
        frame_buttons.pack(pady=5)
        tk.Button(frame_buttons, text="Add product", command=self.open_add_product).pack(side="left", pady=5)
        tk.Button(frame_buttons, text="Modify product", command=self.open_modify_product).pack(side="left", pady=5)
        tk.Button(frame_buttons, text="Delete product", command=self.open_delete_product).pack(side="left", pady=5)

    def open_add_product(self):
        self.frame_lista.pack_forget()
        self.frame_form = product_form.ProductForm(self.container, on_save=self.add_product, on_cancel=self.show_list)
        self.frame_form.pack()

    def add_product(self, data):
        producto_controlador = ProductoControlador()
        producto = producto_controlador.add_product(
            data["nombre"],
            data["categoria"],
            data["precio"],
            data["proveedor"],
            data["variantes"]
        )

        if producto:
            messagebox.showinfo("Success", "Product added successfully")
            self.show_list()
            self.load_productos("")
        else:
            messagebox.showerror("Error", "Failed to add product")


    def show_list(self):
        if hasattr(self, 'frame_form'):
            self.frame_form.destroy()
            self.frame_form = None
        self.frame_lista.pack(fill="both", expand=True)

    def open_modify_product(self):
        pass

    def open_delete_product(self):
        pass

    def list_products(self, productos):
        self.listbox_productos.delete(0, tk.END)
        for producto in productos:
            self.listbox_productos.insert(
                tk.END,
                f"ID: {producto.id} | Nombre: {producto.nombre} | Precio: {producto.precio} | Proveedor: {producto.proveedor} | Categoria: {producto.categoria}"
            )

    def load_productos(self, nombre):
        producto_controlador = ProductoControlador()
        productos = producto_controlador.get_products(nombre)
        self.list_products(productos)

if __name__ == '__main__':
    root = tk.Tk()
    app = MainView(root)
    root.mainloop()
