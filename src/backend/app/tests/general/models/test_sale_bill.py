import pytest
from pydantic import ValidationError

from backend.app.services.general.models.sale_bill import SaleBillCreate, SaleBillOut

def test_sale_bill_create_fields():
    sale = SaleBillCreate(
        ID=1,
        date="2025-06-16",
        state="Completado",
        state_description="Venta finalizada",
        aremany="No",
        units=3,
        income_products=300,
        income_delivery=20,
        cost_sale=30,
        cost_delivery=10,
        refunds=0,
        total=280.0,
        billing_month="2025-06",
        id_client=101
    )
    assert sale.ID == 1
    assert sale.date == "2025-06-16"
    assert sale.state == "Completado"
    assert sale.state_description == "Venta finalizada"
    assert sale.aremany == "No"
    assert sale.units == 3
    assert sale.income_products == 300
    assert sale.income_delivery == 20
    assert sale.cost_sale == 30
    assert sale.cost_delivery == 10
    assert sale.refunds == 0
    assert sale.total == 280
    assert sale.billing_month == "2025-06"
    assert sale.id_client == 101
    assert sale.__entity_name__ == "Venta_Factura"

def test_sale_bill_create_to_dict():
    sale = SaleBillCreate(
        ID=2,
        date="2025-01-01",
        state="Pendiente",
        state_description="Esperando pago",
        aremany="Sí",
        units=1,
        income_products=100.0,
        income_delivery=0.0,
        cost_sale=5.0,
        cost_delivery=0.0,
        refunds=0.0,
        total=95.0,
        billing_month="2025-01",
        id_client=102
    )
    data = sale.to_dict()
    assert data == {
        "ID": 2,
        "date": "2025-01-01",
        "state": "Pendiente",
        "state_description": "Esperando pago",
        "aremany": "Sí",
        "units": 1,
        "income_products": 100.0,
        "income_delivery": 0.0,
        "cost_sale": 5.0,
        "cost_delivery": 0.0,
        "refunds": 0.0,
        "total": 95.0,
        "billing_month": "2025-01",
        "id_client": 102
    }

def test_sale_bill_create_get_fields():
    fields = SaleBillCreate.get_fields()
    assert fields == {
        "ID": "INTEGER PRIMARY KEY",
        "Fecha": "VARCHAR",
        "Estado": "VARCHAR",
        "Descripcion_Estado": "VARCHAR",
        "VariosProductos": "VARCHAR",
        "Unidades": "INTEGER",
        "IngresosProducto": "FLOAT",
        "IngresosEnvio": "FLOAT",
        "CargoVentas": "FLOAT",
        "CostoEnvio": "FLOAT",
        "Anulaciones": "FLOAT",
        "Total": "FLOAT",
        "MesFacturacion": "VARCHAR",
        "IDComprador": "INTEGER"
    }

def test_sale_bill_out_from_dict():
    data = {
        "ID": 3,
        "date": "2025-06-10",
        "state": "Cancelado",
        "state_description": "Cliente desistió",
        "aremany": "No",
        "units": 2,
        "income_products": 50,
        "income_delivery": 5,
        "cost_sale": 3.0,
        "cost_delivery": 2,
        "refunds": 5,
        "total": 45,
        "billing_month": "2025-06",
        "id_client": 103
    }
    sale_out = SaleBillOut.from_dict(data)
    assert isinstance(sale_out, SaleBillOut)
    assert sale_out.ID == 3
    assert sale_out.date == "2025-06-10"
    assert sale_out.state == "Cancelado"
    assert sale_out.state_description == "Cliente desistió"
    assert sale_out.aremany == "No"
    assert sale_out.units == 2
    assert sale_out.income_products == 50
    assert sale_out.income_delivery == 5
    assert sale_out.cost_sale == 3
    assert sale_out.cost_delivery == 2
    assert sale_out.refunds == 5
    assert sale_out.total == 45
    assert sale_out.billing_month == "2025-06"
    assert sale_out.id_client == 103

def test_sale_bill_create_validation_error():
    # Falta el campo obligatorio 'ID'
    with pytest.raises(ValidationError):
        SaleBillCreate(
            date="2025-06-16",
            state="Completado",
            state_description="Venta finalizada",
            aremany="No",
            units=2,
            income_products=100.0,
            income_delivery=10.0,
            cost_sale=5.0,
            cost_delivery=2.0,
            refunds=0.0,
            total=105.0,
            billing_month="2025-06",
            id_client=104
        )