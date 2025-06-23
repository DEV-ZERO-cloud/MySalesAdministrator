from pydantic import BaseModel
class CustomerCreate(BaseModel):
    __entity_name__ = "Producto"
    ID: int #ID
    category: str #Categoria
    sku: str #CodigoSKU
    name: str #Nombre
    codebar: str   #CodigoBarra
    measure_unit: str #UnidadMedidad
    is_available: bool #EsInventariable (Y/N)
    tax_unit: str #ImpuestoCargo (ID)
    retention_unit: str #Retencion (ID)
    description: str    #Descripcion
    stock: int  #Stock
    
    def to_dict(self):
        return self.model_dump()
        
    @classmethod
    def get_fields(cls) -> dict:
        return {
            "CC": "INTEGER PRIMARY KEY",
            "Domicilio": "VARCHAR",
            "Municipio": "VARCHAR",
            "Pais": "VARCHAR",
        }
class CustomerOut(CustomerCreate):
    __entity_name__ = "Producto"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)