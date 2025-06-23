from pydantic import BaseModel
from backend.app.services.inventory_management.models.product_movements import ProductMovement
from typing import List

class StockRegisterCreate(BaseModel):
    __entity_name__ = "RegistroTransaccion"
    id: int
    date: str
    id_store_start: str
    id_store_end: str
    products: List[ProductMovement]

    def to_dict(self):
        # Puedes adaptar esto para serializar la lista de productos si lo necesitas
        return self.model_dump()

    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "Fecha": "VARCHAR",
            "IDBodegaOrigen": "VARCHAR",
            "IDBodegaDestino": "VARCHAR",
        }

class StockRegisterOut(StockRegisterCreate):
    __entity_name__ = "RegistroTransaccion"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)