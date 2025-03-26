import tkinter as tk
from tkinter import messagebox

class ProductForm(tk.Frame):
    def __init__(self, master, product=None, on_save=None, on_cancel=None):

        super().__init__(master)
        self.product = product
        self.on_save = on_save
        self.on_cancel = on_cancel
        self.variants = product.variantes.copy() if product else []
        self.create_widgets()
        if product:
            self.load_data()
    
    def create_widgets(self):
        frame_data = tk.Frame(self)
        frame_data.pack(padx=10, pady=10, fill="x")

        tk.Label(frame_data, text="Nombre:").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(frame_data, width=40)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_data, text="Categoria:").grid(row=1, column=0)
        self.entry_categoria = tk.Entry(frame_data, width=40)
        self.entry_categoria.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_data, text="Precio:").grid(row=2, column=0)
        self.entry_precio = tk.Entry(frame_data, width=40)
        self.entry_precio.grid(row=2, column=1, padx=5, pady=2)

        tk.Label(frame_data, text="Proveedor:").grid(row=3, column=0)
        self.entry_proveedor = tk.Entry(frame_data, width=40)
        self.entry_proveedor.grid(row=3, column=1, padx=5, pady=2)

        frame_variants = tk.LabelFrame(self, text="Variantes")
        frame_variants.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        tk.Label(frame_variants, text="Talla:").grid(row=0, column=0, padx=5, pady=2)
        self.entry_talla = tk.Entry(frame_variants, width=15)
        self.entry_talla.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_variants, text="Color:").grid(row=0, column=4, padx=5, pady=2)
        self.entry_color = tk.Entry(frame_variants, width=15)
        self.entry_color.grid(row=0, column=3, padx=5, pady=2)

        tk.Label(frame_variants, text="Stock:").grid(row=0, column=2, padx=5, pady=2)
        self.entry_stock = tk.Entry(frame_variants, width=15)
        self.entry_stock.grid(row=0, column=5, padx=5, pady=2)

        tk.Button(frame_variants, text="Agregar variante", command=self.add_variant).grid(row=0, column=6, padx=5, pady=2)

        self.listbox_variants = tk.Listbox(frame_variants, width=80, height=5)
        self.listbox_variants.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

        tk.Button(frame_variants, text="Eliminar variante seleccionada", command=self.delete_variant).grid(row=4, column=3)

        tk.Button(self, text="Guardar", command=self.save_product).pack(pady=10, side=tk.LEFT)
        tk.Button(self, text="Cancelar", command=self.cancel).pack(pady=10, side=tk.LEFT)

    def save_product(self):
        pass

    def cancel(self):
        pass

    def delete_variant(self):
        pass

    def creare_widgets(self):
        pass

    def add_variant(self):
        pass

    def load_data():
        pass