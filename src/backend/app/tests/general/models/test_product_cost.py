import pytest
from pydantic import ValidationError

from backend.app.services.general.models.product_cost import ProductCostCreate, ProductCostOut

def test_product_cost_create_fields():
    product = ProductCostCreate(
        ID=10,
        cost=199,
        description="Producto premium",
        year=2024
    )
    assert product.ID == 10
    assert product.cost == 199
    assert product.description == "Producto premium"
    assert product.year == 2024
    assert product.__entity_name__ == "Producto_Costo"

def test_product_cost_create_to_dict():
    product = ProductCostCreate(
        ID=5,
        cost=50.0,
        description="Producto básico",
        year=2023
    )
    data = product.to_dict()
    assert data == {
        "ID": 5,
        "cost": 50.0,
        "description": "Producto básico",
        "year": 2023
    }

def test_product_cost_create_get_fields():
    fields = ProductCostCreate.get_fields()
    assert fields == {
        "ID": "INTEGER PRIMARY KEY",
        "CostoDirecto": "float",
        "Descripcion": "VARCHAR",
        "Año": "VARCHAR"
    }

def test_product_cost_out_from_dict():
    data = {
        "ID": 7,
        "cost": 15,
        "description": "Producto de prueba",
        "year": 2022
    }
    product_out = ProductCostOut.from_dict(data)
    assert isinstance(product_out, ProductCostOut)
    assert product_out.ID == 7
    assert product_out.cost == 15
    assert product_out.description == "Producto de prueba"
    assert product_out.year == 2022

def test_product_cost_create_validation_error():
    # Falta el campo obligatorio 'ID'
    with pytest.raises(ValidationError):
        ProductCostCreate(
            cost=10.0,
            description="Falta ID",
            year=2021
        )