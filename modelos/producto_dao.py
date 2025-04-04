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

    def list_objects(self, nombre):
        try:
            with get_connection() as connection:
                lista_productos = []
                cursor = connection.cursor()
                if nombre:
                    cursor.execute("SELECT * FROM productos WHERE nombre LIKE ?", (f"{nombre}%",))
                else:
                    cursor.execute("SELECT * FROM productos")

                # Manera "Profesional" de hacerlo
                # query = "SELECT * FROM productos WHERE nombre LIKE ?" if nombre else "SELECT * FROM productos"
                # params = (f"{nombre}%",) if nombre else ()
                # cursor.execute(query, params)

                productos = cursor.fetchall()
                for producto in productos:
                    cursor.execute("SELECT  talla, stock, color FROM variantes WHERE productos_id = ?", (producto[0],))
                    variantes = [{"talla": variante[0], "stock": variante[1], "color": variante[2]} for variante in cursor.fetchall()]
                    producto = Producto(producto[1], producto[2], producto[3], producto[4], producto[0], variantes)
                    lista_productos.append(producto)
                return lista_productos
            
        except Exception as e:
            print(f"Error al obtener los productos: {e}")
            return []

    def get_object_by_id(self, id):
        try:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM productos WHERE id = ?", (id,))
                producto = cursor.fetchone()
                if producto:
                    cursor.execute("SELECT talla, stock, color FROM variantes WHERE productos_id = ?", (producto[0],))
                    variantes = [{"talla": variante[0], "stock": variante[1], "color": variante[2]} for variante in cursor.fetchall()]
                    return Producto(producto[1], producto[2], producto[3], producto[4], producto[0], variantes)
                return None
            
        except Exception as e:
            print(f"Error al obtener el producto por ID: {e}")
            return None
    
    def update_object(self, producto):
        try:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE productos
                    SET nombre = ?, categoria = ?, precio = ?, proveedor = ? 
                    WHERE id = ?""", (producto.nombre, producto.categoria, producto.precio, producto.proveedor, producto.id))
                
                connection.commit()
            
            return producto

        except Exception as e:
            print(f"[!] Error al actualizar el producto: {e}")
            return None

    def delete_object(self, id):
        try:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
                connection.commit()
            
        except Exception as e:
            print(f"[!] Error al eliminar el producto: {e}")
            return None

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
        
    def delete_variants(self, id):
        try:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM variantes WHERE productos_id = ?", (id,))
                connection.commit()
            
        except Exception as e:
            print(f"[!] Error al eliminar la variante: {e}")
            return None
        
    def update_variante(self, variante, id):
        try:
            with get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO variantes (productos_id, talla, stock, color) 
                    VALUES (?, ?, ?, ?)""", (id, variante.talla, variante.stock, variante.color))
                    
                connection.commit()
        except Exception as e:
            print(f"[!] Error al actualizar las variantes: {e}")
            return None

