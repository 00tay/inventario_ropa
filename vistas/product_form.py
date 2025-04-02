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

        tk.Label(frame_variants, text="Color:").grid(row=0, column=2, padx=5, pady=2)
        self.entry_color = tk.Entry(frame_variants, width=15)
        self.entry_color.grid(row=0, column=3, padx=5, pady=2)

        tk.Label(frame_variants, text="Stock:").grid(row=0, column=4, padx=5, pady=2)
        self.entry_stock = tk.Entry(frame_variants, width=15)
        self.entry_stock.grid(row=0, column=5, padx=5, pady=2)

        tk.Button(frame_variants, text="Agregar variante", command=self.add_variant).grid(row=0, column=6, padx=5, pady=2)

        self.listbox_variants = tk.Listbox(frame_variants, width=80, height=5, selectmode=tk.MULTIPLE)
        self.listbox_variants.grid(row=1, column=0, columnspan=7, padx=5, pady=5)

        tk.Button(frame_variants, text="Eliminar variante seleccionada", command=self.delete_variant).grid(row=4, column=3)

        tk.Button(self, text="Guardar", command=self.save_product).pack(pady=10, side=tk.LEFT)
        tk.Button(self, text="Cancelar", command=self.cancel).pack(pady=10, side=tk.LEFT)

    def save_product(self):
        nombre = self.entry_nombre.get().strip()
        categoria = self.entry_categoria.get().strip()
        precio = self.entry_precio.get().strip()
        proveedor = self.entry_proveedor.get().strip()

        if not nombre or not precio or not proveedor:
            messagebox.showerror("Error", "Por favor complete todos los campos obligatorios, Precio, Proveedor y Nombre.")
            return
        try:
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser un número.")
            return

        data = {
            'nombre': nombre,
            'categoria': categoria,
            'precio': precio,
            'proveedor': proveedor,
            'variantes': self.variants
        }
        
        if self.product:
            if self.on_save:
                self.on_save(data, self.product.id)
        else:
            if self.on_save:
                self.on_save(data)

    def add_variant(self):
        talla = self.entry_talla.get().strip()
        color = self.entry_color.get().strip()
        stock_str = self.entry_stock.get().strip()

        if not talla or not color or not stock_str:
            messagebox.showerror("Error", "Por favor complete todos los campos de la variante.")
            return

        try:
            stock = int(stock_str)
        except ValueError:
            messagebox.showerror("Error", "El stock debe ser un número entero.")
            return

        variante = {
            'talla': talla,
            'color': color,
            'stock': stock
        }

        self.variants.append(variante)

        self.entry_talla.delete(0, tk.END)
        self.entry_talla.focus()

        self.entry_color.bind("<FocusIn>", lambda event: self.entry_color.delete(0, tk.END))
        self.entry_stock.bind("<FocusIn>", lambda event: self.entry_stock.delete(0, tk.END))

        self.reload_listbox()

    def reload_listbox(self):
        self.listbox_variants.delete(0, tk.END)
        for idx, variant in enumerate(self.variants):
            self.listbox_variants.insert(tk.END,f"{idx+1}.  Talla: {variant['talla']} | Color: {variant['color']} | Stock: {variant['stock']}")

    def cancel(self):
        if self.on_cancel:
            self.on_cancel()

    def delete_variant(self):
        variantes = self.listbox_variants.curselection()
        if variantes:
            for variante in reversed(variantes):
                del self.variants[variante]
            self.reload_listbox()
        else:
            messagebox.showerror("Error", "Seleccione una variante para eliminar.")

    def load_data(self):
        self.entry_nombre.insert(0, self.product.nombre)
        self.entry_categoria.insert(0, self.product.categoria)
        self.entry_precio.insert(0, self.product.precio)
        self.entry_proveedor.insert(0, self.product.proveedor)
        self.reload_listbox()
