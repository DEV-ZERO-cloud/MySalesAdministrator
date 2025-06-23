from pydantic import BaseModel
class StoreCreate(BaseModel):
    __entity_name__ = "Bodega"
    ID: int #ID
    category: str #Categoria
    name: str #Nombre
    office_id: str #ID Sucursal
    address: str #Direccion

    def to_dict(self):
        return self.model_dump()
        
    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "Categoria": "VARCHAR",
            "Nombre": "VARCHAR",
            "IDSucursal":"VARCHAR",
            "Direccion":"VARCHAR"
        }
class StoreOut(StoreCreate):
    __entity_name__ = "Bodega"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)