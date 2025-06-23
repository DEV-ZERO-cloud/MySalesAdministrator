import pytest
from backend.app.services.inventory_management.models.service import ServiceCreate, ServiceOut  # Cambia 'your_module' por el nombre real del archivo

def test_service_create():
    service = ServiceCreate(
        ID=1,
        category="Mantenimiento",
        name="Limpieza de PC",
        codebar="SERV123456",
        measure_unit="Unidad",
        is_taxable=True,
        tax_unit="IVA16",
        retention_unit="RET0",
        description="Limpieza interna de computadora",
        price=350.00
    )
    assert service.ID == 1
    assert service.category == "Mantenimiento"
    assert service.name == "Limpieza de PC"
    assert service.codebar == "SERV123456"
    assert service.measure_unit == "Unidad"
    assert service.is_taxable is True
    assert service.tax_unit == "IVA16"
    assert service.retention_unit == "RET0"
    assert service.description == "Limpieza interna de computadora"
    assert service.price == 350.00

def test_to_dict():
    service = ServiceCreate(
        ID=2,
        category="Soporte",
        name="Instalación de software",
        codebar="SERV654321",
        measure_unit="Servicio",
        is_taxable=False,
        tax_unit="IVA0",
        retention_unit="RET0",
        description="Instalación de antivirus y programas",
        price=200.0
    )
    service_dict = service.to_dict()
    assert isinstance(service_dict, dict)
    assert service_dict["ID"] == 2
    assert service_dict["category"] == "Soporte"
    assert service_dict["name"] == "Instalación de software"
    assert service_dict["codebar"] == "SERV654321"
    assert service_dict["measure_unit"] == "Servicio"
    assert service_dict["is_taxable"] is False
    assert service_dict["tax_unit"] == "IVA0"
    assert service_dict["retention_unit"] == "RET0"
    assert service_dict["description"] == "Instalación de antivirus y programas"
    assert service_dict["price"] == 200.0

def test_get_fields():
    fields = ServiceCreate.get_fields()
    assert isinstance(fields, dict)
    assert fields["ID"] == "INTEGER PRIMARY KEY"
    assert fields["Categoria"] == "VARCHAR"
    assert fields["Nombre"] == "VARCHAR"
    assert fields["CodigoBarra"] == "VARCHAR"
    assert fields["UnidadMedida"] == "VARCHAR"
    assert fields["EsGravable"] == "BOOLEAN"
    assert fields["ImpuestoCargo (ID)"] == "VARCHAR"
    assert fields["Retencion (ID)"] == "VARCHAR"
    assert fields["Descripcion"] == "VARCHAR"
    assert fields["Precio"] == "FLOAT"

def test_service_out_from_dict():
    data = {
        "ID": 3,
        "category": "Consultoría",
        "name": "Asesoría técnica",
        "codebar": "SERV999888",
        "measure_unit": "Hora",
        "is_taxable": True,
        "tax_unit": "IVA8",
        "retention_unit": "RET1",
        "description": "Consultoría en sistemas informáticos",
        "price": 500.0
    }
    service = ServiceOut.from_dict(data)
    assert isinstance(service, ServiceOut)
    assert service.ID == 3
    assert service.category == "Consultoría"
    assert service.name == "Asesoría técnica"
    assert service.codebar == "SERV999888"
    assert service.measure_unit == "Hora"
    assert service.is_taxable is True
    assert service.tax_unit == "IVA8"
    assert service.retention_unit == "RET1"
    assert service.description == "Consultoría en sistemas informáticos"
    assert service.price == 500.0