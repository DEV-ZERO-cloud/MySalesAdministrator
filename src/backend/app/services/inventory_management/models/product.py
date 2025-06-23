from pydantic import BaseModel
class ProductCreate(BaseModel):
    __entity_name__ = "Producto"
    ID: int #ID
    category: str #Categoria
    sku: str #CodigoSKU
    name: str #Nombre
    codebar: str   #CodigoBarra
    measure_unit: str #UnidadMedida
    is_available: bool #EsInventariable (Y/N)
    is_taxable: bool #EsGravable(IVA) (Y/N)
    tax_unit: str #ImpuestoCargo (ID)
    retention_unit: str #Retencion (ID)
    description: str    #Descripcion
    stock: int  #Stock
    price: float #Precio
    
    def to_dict(self):
        return self.model_dump()
        
    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "Categoria": "VARCHAR",
            "CodigoSKU": "VARCHAR",
            "Nombre": "VARCHAR",
            "CodigoBarra": "VARCHAR",
            "UnidadMedida": "VARCHAR",
            "EsInventariable": "BOOLEAN",
            "EsGravable": "BOOLEAN",
            "ImpuestoCargo (ID)": "VARCHAR",
            "Retencion (ID)": "VARCHAR",
            "Descripcion": "VARCHAR",
            "Stock": "INTEGER",
            "Precio": "FLOAT"
        }
class ProductOut(ProductCreate):
    __entity_name__ = "Producto"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)