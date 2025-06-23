import pytest
from pydantic import ValidationError

from backend.app.services.general.models.product_publishment import ProductCostCreate, ProductCostOut

def test_product_cost_create_fields():
    product = ProductCostCreate(
        ID=100,
        sales_channel="Online",
        name="Producto Estrella",
        variant="Color Rojo",
        unit_price=299,
        publisment_type="Destacada"
    )
    assert product.ID == 100
    assert product.sales_channel == "Online"
    assert product.name == "Producto Estrella"
    assert product.variant == "Color Rojo"
    assert product.unit_price == 299
    assert product.publisment_type == "Destacada"
    assert product.__entity_name__ == "Producto_Publicacion"

def test_product_cost_create_to_dict():
    product = ProductCostCreate(
        ID=101,
        sales_channel="Tienda Física",
        name="Producto Básico",
        variant="Sin variante",
        unit_price=49.99,
        publisment_type="Común"
    )
    data = product.to_dict()
    assert data == {
        "ID": 101,
        "sales_channel": "Tienda Física",
        "name": "Producto Básico",
        "variant": "Sin variante",
        "unit_price": 49.99,
        "publisment_type": "Común"
    }

def test_product_cost_create_get_fields():
    fields = ProductCostCreate.get_fields()
    assert fields == {
        "ID": "INTEGER PRIMARY KEY",
        "Canal_venta": "VARCHAR",
        "Titulo": "VARCHAR",
        "Variante": "VARCHAR",
        "Precio_unitario_venta": "FLOAT",
        "Tipo_publicacion": "VARCHAR"
    }

def test_product_cost_out_from_dict():
    data = {
        "ID": 102,
        "sales_channel": "Marketplace",
        "name": "Producto de Prueba",
        "variant": "Tamaño XL",
        "unit_price": 120,
        "publisment_type": "Premium"
    }
    product_out = ProductCostOut.from_dict(data)
    assert isinstance(product_out, ProductCostOut)
    assert product_out.ID == 102
    assert product_out.sales_channel == "Marketplace"
    assert product_out.name == "Producto de Prueba"
    assert product_out.variant == "Tamaño XL"
    assert product_out.unit_price == 120
    assert product_out.publisment_type == "Premium"

def test_product_cost_create_validation_error():
    # Falta el campo obligatorio 'ID'
    with pytest.raises(ValidationError):
        ProductCostCreate(
            sales_channel="Online",
            name="Producto Error",
            variant="Sin variante",
            unit_price=10.0,
            publisment_type="Común"
        )