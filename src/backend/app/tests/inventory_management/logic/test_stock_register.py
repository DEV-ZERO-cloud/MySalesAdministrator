import pytest
from backend.app.services.inventory_management.logic.stock_register import StockRegister  # Cambia el import si tu archivo tiene otro nombre

def test_stock_register_initialization_and_getters():
    reg = StockRegister(
        id=1,
        date="2025-06-23",
        id_store_start="S001",
        id_store_end="S002",
        id_product="P001",
        quantity=10
    )
    assert reg.id == 1
    assert reg.date == "2025-06-23"
    assert reg.id_store_start == "S001"
    assert reg.id_store_end == "S002"
    assert reg.id_product == "P001"
    assert reg.quantity == 10

def test_stock_register_setters():
    reg = StockRegister(1, "2025-06-23", "S001", "S002", "P001", 10)
    reg.id = 2
    reg.date = "2025-07-01"
    reg.id_store_start = "S010"
    reg.id_store_end = "S020"
    reg.id_product = "P999"
    reg.quantity = 99

    assert reg.id == 2
    assert reg.date == "2025-07-01"
    assert reg.id_store_start == "S010"
    assert reg.id_store_end == "S020"
    assert reg.id_product == "P999"
    assert reg.quantity == 99