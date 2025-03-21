from modelos.producto import Producto, Variante
from modelos.db import get_connection

class ProductoDao:
    
    def add_object(self, producto):
        try:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO productos (nombre, categoria, precio, proveedor) 
                    VALUES (?, ?, ?, ?)""", (producto.nombre, producto.categoria, producto.precio, producto.proveedor))
                producto.id = cursor.lastrowid
                connection.commit()
                return producto

        except Exception as e:
            print(f"[!] Error al agregar el producto: {e}")
            return None

    def get_object(self, producto_id):
        try:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
                producto_data = cursor.fetchone()
                if producto_data:
                    producto = Producto(*producto_data)

                    cursor.execute("SELECT * FROM variantes WHERE productos_id = ?", (producto_id,))
                    variantes_data = cursor.fetchall()
                    for variante_data in variantes_data:
                        variante = Variante(*variante_data)
                        producto.variantes.append(variante)

                    return producto
                return None
            
        except Exception as e:
            print(f"[!] Error al obtener el producto: {e}")
            return None

    def list_objects(self):
        try:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT id, nombre, categoria, precio, proveedor FROM productos")
                productos = cursor.fetchall()
                lista_productos = []
                for producto in productos:
                    cursor.execute("SELECT  talla, stock, color FROM variantes WHERE productos_id = ?", (producto[0],))
                    variantes = [{"talla": variante[0], "stock": variante[1], "color": variante[2]} for variante in cursor.fetchall()]
                    producto = Producto(producto[1], producto[2], producto[3], producto[4], producto[0], variantes)
                    lista_productos.append(producto)
                return lista_productos
            
        except Exception as e:
            print(f"Error al obtener los productos: {e}")
            return []
        
class VarianteDao:
    def agregar_variante(self, variante, producto_id):
        try:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO variantes (productos_id, talla, stock, color) 
                    VALUES (?, ?, ?, ?)""", (producto_id, variante.talla, variante.stock, variante.color))
                variante.id = cursor.lastrowid
                connection.commit()
                return variante
            
        except Exception as e:
            print(f"[!] Error al agregar la variante: {e}")
            return None
