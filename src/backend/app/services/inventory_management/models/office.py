from pydantic import BaseModel
class OfficeCreate(BaseModel):
    __entity_name__ = "Sucursal"
    ID: int #ID
    category: str #Categoria
    name: str #Nombre
    address: str #Direccion
    phone: str  #TelefonoGeneral

    def to_dict(self):
        return self.model_dump()
        
    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "Categoria": "VARCHAR",
            "Nombre": "VARCHAR",
            "IDSucursal":"VARCHAR",
            "Direccion":"VARCHAR",
            "TelefonoGeneral":"VARCHAR"
        }
class OfficeOut(OfficeCreate):
    __entity_name__ = "Sucursal"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)