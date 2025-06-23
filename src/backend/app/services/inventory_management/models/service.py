from pydantic import BaseModel
class ServiceCreate(BaseModel):
    __entity_name__ = "Servicio"
    ID: int #ID
    category: str #Categoria
    name: str #Nombre
    codebar: str   #CodigoBarra
    measure_unit: str #UnidadMedida
    is_taxable: bool #EsGravable(IVA) (Y/N)
    tax_unit: str #ImpuestoCargo (ID)
    retention_unit: str #Retencion (ID)
    description: str    #Descripcion
    price: float #Precio
    
    def to_dict(self):
        return self.model_dump()
        
    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "Categoria": "VARCHAR",
            "Nombre": "VARCHAR",
            "CodigoBarra": "VARCHAR",
            "UnidadMedida": "VARCHAR",
            "EsGravable": "BOOLEAN",
            "ImpuestoCargo (ID)": "VARCHAR",
            "Retencion (ID)": "VARCHAR",
            "Descripcion": "VARCHAR",
            "Precio": "FLOAT"
        }
class ServiceOut(ServiceCreate):
    __entity_name__ = "Servicio"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)