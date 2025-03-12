import  modelos.db as db
from modelos.producto import Producto, Variante
from controladores.producto_controlador import ProductoControlador

if __name__ == '__main__':
    db.init_db()
    producto = ProductoControlador()
    producto.add_product("Taparabos", "Ropa Interior", 500, "Puma", [{"talla": "XXL", "color": "Violeta", "stock": 1}, {"talla": "L", "color": "Rojo", "stock":2}],)