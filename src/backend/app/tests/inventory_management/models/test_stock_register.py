import pytest
from stock_register_model import StockRegisterCreate, StockRegisterOut

def test_stock_register_create_to_dict():
    reg = StockRegisterCreate(
        id=1,
        date="2025-06-23",
        id_store_start="B001",
        id_store_end="B002",
        id_product="P123",
        quantity=100
    )
    reg_dict = reg.to_dict()
    assert isinstance(reg_dict, dict)
    assert reg_dict["id"] == 1
    assert reg_dict["date"] == "2025-06-23"
    assert reg_dict["id_store_start"] == "B001"
    assert reg_dict["id_store_end"] == "B002"
    assert reg_dict["id_product"] == "P123"
    assert reg_dict["quantity"] == 100

def test_stock_register_create_get_fields():
    fields = StockRegisterCreate.get_fields()
    assert isinstance(fields, dict)
    assert fields["ID"] == "INTEGER PRIMARY KEY"
    assert fields["Fecha"] == "VARCHAR"
    assert fields["IDBodegaOrigen"] == "VARCHAR"
    assert fields["IDBodegaDestino"] == "VARCHAR"
    assert fields["IDProducto"] == "VARCHAR"
    assert fields["Cantidad"] == "INTEGER"

def test_stock_register_out_from_dict():
    data = {
        "id": 2,
        "date": "2025-07-01",
        "id_store_start": "B010",
        "id_store_end": "B020",
        "id_product": "P555",
        "quantity": 50
    }
    reg = StockRegisterOut.from_dict(data)
    assert isinstance(reg, StockRegisterOut)
    assert reg.id == 2
    assert reg.date == "2025-07-01"
    assert reg.id_store_start == "B010"
    assert reg.id_store_end == "B020"
    assert reg.id_product == "P555"
    assert reg.quantity == 50