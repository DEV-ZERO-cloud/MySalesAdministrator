import pytest
from backend.app.services.inventory_management.models.office import OfficeCreate, OfficeOut  # Cambia 'your_module' por el nombre real del archivo

def test_office_create():
    office = OfficeCreate(
        ID=1,
        category="Principal",
        name="Sucursal Centro",
        address="Calle 123",
        phone="555-1234"
    )
    assert office.ID == 1
    assert office.category == "Principal"
    assert office.name == "Sucursal Centro"
    assert office.address == "Calle 123"
    assert office.phone == "555-1234"

def test_to_dict():
    office = OfficeCreate(
        ID=2,
        category="Secundaria",
        name="Sucursal Sur",
        address="Avenida 456",
        phone="555-5678"
    )
    office_dict = office.to_dict()
    assert isinstance(office_dict, dict)
    assert office_dict["ID"] == 2
    assert office_dict["category"] == "Secundaria"
    assert office_dict["name"] == "Sucursal Sur"
    assert office_dict["address"] == "Avenida 456"
    assert office_dict["phone"] == "555-5678"

def test_get_fields():
    fields = OfficeCreate.get_fields()
    assert isinstance(fields, dict)
    assert fields["ID"] == "INTEGER PRIMARY KEY"
    assert fields["Categoria"] == "VARCHAR"
    assert fields["Nombre"] == "VARCHAR"
    assert fields["IDSucursal"] == "VARCHAR"
    assert fields["Direccion"] == "VARCHAR"
    assert fields["TelefonoGeneral"] == "VARCHAR"

def test_office_out_from_dict():
    data = {
        "ID": 3,
        "category": "Tercera",
        "name": "Sucursal Norte",
        "address": "Boulevard 789",
        "phone": "555-9012"
    }
    office = OfficeOut.from_dict(data)
    assert isinstance(office, OfficeOut)
    assert office.ID == 3
    assert office.category == "Tercera"
    assert office.name == "Sucursal Norte"
    assert office.address == "Boulevard 789"
    assert office.phone == "555-9012"