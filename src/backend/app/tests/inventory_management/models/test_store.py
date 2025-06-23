import pytest
from backend.app.services.inventory_management.models.store import StoreCreate, StoreOut  # Cambia 'your_module' por el nombre real del archivo

def test_store_create():
    store = StoreCreate(
        ID=1,
        category="General",
        name="Bodega Central",
        office_id="SUC123",
        address="Av. Siempre Viva 123"
    )
    assert store.ID == 1
    assert store.category == "General"
    assert store.name == "Bodega Central"
    assert store.office_id == "SUC123"
    assert store.address == "Av. Siempre Viva 123"

def test_to_dict():
    store = StoreCreate(
        ID=2,
        category="Electrónica",
        name="Bodega Norte",
        office_id="SUC456",
        address="Calle 456"
    )
    store_dict = store.to_dict()
    assert isinstance(store_dict, dict)
    assert store_dict["ID"] == 2
    assert store_dict["category"] == "Electrónica"
    assert store_dict["name"] == "Bodega Norte"
    assert store_dict["office_id"] == "SUC456"
    assert store_dict["address"] == "Calle 456"

def test_get_fields():
    fields = StoreCreate.get_fields()
    assert isinstance(fields, dict)
    assert fields["ID"] == "INTEGER PRIMARY KEY"
    assert fields["Categoria"] == "VARCHAR"
    assert fields["Nombre"] == "VARCHAR"
    assert fields["IDSucursal"] == "VARCHAR"
    assert fields["Direccion"] == "VARCHAR"

def test_store_out_from_dict():
    data = {
        "ID": 3,
        "category": "Alimentos",
        "name": "Bodega Sur",
        "office_id": "SUC789",
        "address": "Boulevard 789"
    }
    store = StoreOut.from_dict(data)
    assert isinstance(store, StoreOut)
    assert store.ID == 3
    assert store.category == "Alimentos"
    assert store.name == "Bodega Sur"
    assert store.office_id == "SUC789"
    assert store.address == "Boulevard 789"