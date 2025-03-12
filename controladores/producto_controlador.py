from modelos.producto import Producto, Variante
from modelos.producto_dao import ProductoDao, VarianteDao

class ProductoControlador:
    def add_product(self, nombre, categoria, precio, proveedor, variantes_data):
        producto = Producto(nombre, categoria, precio, proveedor)
        producto_dao = ProductoDao()
        producto =  producto_dao.add_object(producto)

        if producto:
            variante_dao = VarianteDao()
            for variante_data in variantes_data:
                variante = Variante(**variante_data)
                variante = variante_dao.agregar_variante(variante, producto.id)
                if variante:
                    producto.variantes.append(variante)
            return producto
        return None

