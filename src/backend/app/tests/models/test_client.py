import pytest
from pydantic import ValidationError

from models.client import CustomerCreate, CustomerOut

def test_customer_create_fields():
    customer = CustomerCreate(
        ID=123,
        name="Juan Perez",
        address="Calle 123",
        city="Bogotá",
        country="Colombia"
    )
    assert customer.ID == 123
    assert customer.name == "Juan Perez"
    assert customer.address == "Calle 123"
    assert customer.city == "Bogotá"
    assert customer.country == "Colombia"
    assert customer.__entity_name__ == "Comprador"

def test_customer_create_to_dict():
    customer = CustomerCreate(
        ID=1,
        name="Andres",
        address="Av. Principal",
        city="Medellín",
        country="Colombia"
    )
    data = customer.to_dict()
    assert data == {
        "ID": 1,
        "name": "Andres",
        "address": "Av. Principal",
        "city": "Medellín",
        "country": "Colombia"
    }

def test_customer_create_get_fields():
    fields = CustomerCreate.get_fields()
    assert fields == {
        "CC": "INTEGER PRIMARY KEY",
        "Domicilio": "VARCHAR",
        "Municipio": "VARCHAR",
        "Pais": "VARCHAR"
    }

def test_customer_out_from_dict():
    data = {
        "ID": 42,
        "name": "Ana",
        "address": "Carrera 9",
        "city": "Cali",
        "country": "Colombia"
    }
    customer_out = CustomerOut.from_dict(data)
    assert isinstance(customer_out, CustomerOut)
    assert customer_out.ID == 42
    assert customer_out.name == "Ana"
    assert customer_out.address == "Carrera 9"
    assert customer_out.city == "Cali"
    assert customer_out.country == "Colombia"

def test_customer_create_validation_error():
    # Falta el campo obligatorio 'ID'
    with pytest.raises(ValidationError):
        CustomerCreate(
            name="Mario",
            address="Calle Falsa",
            city="Barranquilla",
            country="Colombia"
        )