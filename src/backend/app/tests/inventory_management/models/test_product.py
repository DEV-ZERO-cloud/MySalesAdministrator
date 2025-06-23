import pytest
from backend.app.services.inventory_management.models.product import ProductCreate, ProductOut  # Cambia 'your_module' por el nombre real del archivo

def test_product_create():
    product = ProductCreate(
        ID=1,
        category="Bebidas",
        sku="SKU123",
        name="Coca Cola",
        codebar="1234567890123",
        measure_unit="Lata",
        is_available=True,
        is_taxable=True,
        tax_unit="IVA16",
        retention_unit="RET0",
        description="Bebida gaseosa",
        stock=100,
        price=15.5
    )
    assert product.ID == 1
    assert product.category == "Bebidas"
    assert product.sku == "SKU123"
    assert product.name == "Coca Cola"
    assert product.codebar == "1234567890123"
    assert product.measure_unit == "Lata"
    assert product.is_available is True
    assert product.is_taxable is True
    assert product.tax_unit == "IVA16"
    assert product.retention_unit == "RET0"
    assert product.description == "Bebida gaseosa"
    assert product.stock == 100
    assert product.price == 15.5

def test_to_dict():
    product = ProductCreate(
        ID=2,
        category="Snacks",
        sku="SKU456",
        name="Papas Fritas",
        codebar="9876543210987",
        measure_unit="Bolsa",
        is_available=False,
        is_taxable=False,
        tax_unit="IVA0",
        retention_unit="RET0",
        description="Snacks de papa",
        stock=50,
        price=10.0
    )
    product_dict = product.to_dict()
    assert isinstance(product_dict, dict)
    assert product_dict["ID"] == 2
    assert product_dict["category"] == "Snacks"
    assert product_dict["sku"] == "SKU456"
    assert product_dict["name"] == "Papas Fritas"
    assert product_dict["codebar"] == "9876543210987"
    assert product_dict["measure_unit"] == "Bolsa"
    assert product_dict["is_available"] is False
    assert product_dict["is_taxable"] is False
    assert product_dict["tax_unit"] == "IVA0"
    assert product_dict["retention_unit"] == "RET0"
    assert product_dict["description"] == "Snacks de papa"
    assert product_dict["stock"] == 50
    assert product_dict["price"] == 10.0

def test_get_fields():
    fields = ProductCreate.get_fields()
    assert isinstance(fields, dict)
    assert fields["ID"] == "INTEGER PRIMARY KEY"
    assert fields["Categoria"] == "VARCHAR"
    assert fields["CodigoSKU"] == "VARCHAR"
    assert fields["Nombre"] == "VARCHAR"
    assert fields["CodigoBarra"] == "VARCHAR"
    assert fields["UnidadMedida"] == "VARCHAR"
    assert fields["EsInventariable"] == "BOOLEAN"
    assert fields["EsGravable"] == "BOOLEAN"
    assert fields["ImpuestoCargo (ID)"] == "VARCHAR"
    assert fields["Retencion (ID)"] == "VARCHAR"
    assert fields["Descripcion"] == "VARCHAR"
    assert fields["Stock"] == "INTEGER"
    assert fields["Precio"] == "FLOAT"

def test_product_out_from_dict():
    data = {
        "ID": 3,
        "category": "Lácteos",
        "sku": "SKU789",
        "name": "Leche Entera",
        "codebar": "1112223334445",
        "measure_unit": "Litro",
        "is_available": True,
        "is_taxable": False,
        "tax_unit": "IVA0",
        "retention_unit": "RET0",
        "description": "Leche entera pasteurizada",
        "stock": 200,
        "price": 22.0
    }
    product = ProductOut.from_dict(data)
    assert isinstance(product, ProductOut)
    assert product.ID == 3
    assert product.category == "Lácteos"
    assert product.sku == "SKU789"
    assert product.name == "Leche Entera"
    assert product.codebar == "1112223334445"
    assert product.measure_unit == "Litro"
    assert product.is_available is True
    assert product.is_taxable is False
    assert product.tax_unit == "IVA0"
    assert product.retention_unit == "RET0"
    assert product.description == "Leche entera pasteurizada"
    assert product.stock == 200
    assert product.price == 22.0