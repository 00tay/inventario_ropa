from modelos.producto_dao import ProductoDao as pd, VarianteDao as vd

def test_add_object():
    producto = pd().add_object("Toni Corra", "Ropa Interior", 500, "Puma")
    assert producto.id is not None
    assert producto.nombre == "Toni Corra"
    assert producto.categoria == "Ropa Interior"
    assert producto.precio == 500

def test_get_object():
    producto = pd().get_object(1)
    assert producto.id == 1
    assert producto.nombre == "Toni Corra"
    assert producto.categoria == "Ropa Interior"
    assert producto.precio == 500
    assert producto.proveedor == "Puma"
    assert len(producto.variantes) == 2
    assert producto.variantes[0].talla == "XXL"
    assert producto.variantes[0].color == "Violeta"
    assert producto.variantes[0].stock == 1
    assert producto.variantes[1].talla == "L"
    assert producto.variantes[1].color == "Rojo"
    assert producto.variantes[1].stock == 2 

def test_agregar_variante():
    variante = vd().agregar_variante
    assert variante.id is not None
    assert variante.talla == "XL"
    assert variante.color == "Azul"
    assert variante.stock == 3