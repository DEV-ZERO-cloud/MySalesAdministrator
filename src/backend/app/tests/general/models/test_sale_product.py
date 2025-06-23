import pytest
from pydantic import ValidationError

from backend.app.services.general.models.sale_product import SaleBillCreate, SaleBillOut

def test_sale_bill_create_fields():
    sale = SaleBillCreate(
        ID=1,
        IDProduct=10,
        units=2,
        percentage=50,
        income_products=200,
        income_delivery=15,
        cost_sale=20,
        cost_delivery=5,
        refunds=0.0,
        total=190.0
    )
    assert sale.ID == 1
    assert sale.IDProduct == 10
    assert sale.units == 2
    assert sale.percentage == 50
    assert sale.income_products == 200
    assert sale.income_delivery == 15
    assert sale.cost_sale == 20
    assert sale.cost_delivery == 5
    assert sale.refunds == 0
    assert sale.total == 190
    assert sale.__entity_name__ == "Venta_Producto"

def test_sale_bill_create_to_dict():
    sale = SaleBillCreate(
        ID=2,
        IDProduct=11,
        units=5,
        percentage=80.0,
        income_products=300.0,
        income_delivery=25.0,
        cost_sale=30.0,
        cost_delivery=7.0,
        refunds=2.0,
        total=286.0
    )
    data = sale.to_dict()
    assert data == {
        "ID": 2,
        "IDProduct": 11,
        "units": 5,
        "percentage": 80.0,
        "income_products": 300.0,
        "income_delivery": 25.0,
        "cost_sale": 30.0,
        "cost_delivery": 7.0,
        "refunds": 2.0,
        "total": 286.0
    }

def test_sale_bill_create_get_fields():
    fields = SaleBillCreate.get_fields()
    assert fields == {
        "ID": "INTEGER PRIMARY KEY",
        "IDProductoPublicacion": "INTEGER",
        "Unidades": "INTEGER",
        "IngresosProducto": "FLOAT",
        "IngresosEnvio": "FLOAT",
        "CargoVentas": "FLOAT",
        "CostoEnvio": "FLOAT",
        "Anulaciones": "FLOAT",
        "Total": "FLOAT",
    }

def test_sale_bill_out_from_dict():
    data = {
        "ID": 3,
        "IDProduct": 12,
        "units": 1,
        "percentage": 100,
        "income_products": 100,
        "income_delivery": 10,
        "cost_sale": 5,
        "cost_delivery": 2,
        "refunds": 0,
        "total": 103
    }
    sale_out = SaleBillOut.from_dict(data)
    assert isinstance(sale_out, SaleBillOut)
    assert sale_out.ID == 3
    assert sale_out.IDProduct == 12
    assert sale_out.units == 1
    assert sale_out.percentage == 100
    assert sale_out.income_products == 100
    assert sale_out.income_delivery == 10
    assert sale_out.cost_sale == 5
    assert sale_out.cost_delivery == 2
    assert sale_out.refunds == 0
    assert sale_out.total == 103

def test_sale_bill_create_validation_error():
    # Falta el campo obligatorio 'ID'
    with pytest.raises(ValidationError):
        SaleBillCreate(
            IDProduct=13,
            units=2,
            percentage=60.0,
            income_products=120.0,
            income_delivery=12.0,
            cost_sale=6.0,
            cost_delivery=1.0,
            refunds=0.0,
            total=125.0
        )