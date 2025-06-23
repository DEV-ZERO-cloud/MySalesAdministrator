from pydantic import BaseModel
class ProductCostCreate(BaseModel):
    __entity_name__ = "Producto_Costo"
    ID: int #ID
    cost: float #CostoDirecto
    description: str #Descripcion
    year: int   #Año

    def to_dict(self):
        return self.model_dump()
        
    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "CostoDirecto": "float",
            "Descripcion": "VARCHAR",
            "Año": "VARCHAR",
        }
class ProductCostOut(ProductCostCreate):
    __entity_name__ = "Producto_Costo"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)