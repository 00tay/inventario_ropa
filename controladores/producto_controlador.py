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

    def update_product(self, nombre, categoria, precio, proveedor, id, variantes_data):
        producto = Producto(nombre, categoria, precio, proveedor, id)
        producto_dao = ProductoDao()
        producto = producto_dao.update_object(producto)
        if producto:
            variante_dao = VarianteDao()
            variante_dao.delete_variants(producto.id)
            for variante_data in variantes_data:
                variante = Variante(**variante_data)
                variante = variante_dao.update_variante(variante, producto.id)
            return producto

    def get_products(self, nombre):
        producto = ProductoDao()
        producto = producto.list_objects(nombre)
        return producto

    def get_product_by_id(self, id):
        producto = ProductoDao()
        producto = producto.get_object_by_id(id)
        return producto
    
    def delete_product(self, id):
        producto = ProductoDao()
        producto = producto.delete_object(id)
        return producto
