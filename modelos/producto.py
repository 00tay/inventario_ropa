class Producto:
    
    def __init__(self, nombre, categoria, precio, proveedor, id=None, variantes=[]):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.proveedor = proveedor
        self.variantes = variantes

class Variante:
    
    def __init__(self, talla, color, stock, id=None):
        self.id = id
        self.talla = talla
        self.color = color
        self.stock = stock
    