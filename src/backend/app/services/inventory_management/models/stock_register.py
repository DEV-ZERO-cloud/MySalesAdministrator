from pydantic import BaseModel

class StockRegisterCreate(BaseModel):
    __entity_name__ = "RegistroTransaccion"
    id: int  # ID
    date: str  # Fecha
    id_store_start: str  # ID Bodega Origen
    id_store_end: str    # ID Bodega Destino
    id_product: str      # ID Producto
    quantity: int        # Cantidad

    def to_dict(self):
        return self.model_dump()

    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "Fecha": "VARCHAR",
            "IDBodegaOrigen": "VARCHAR",
            "IDBodegaDestino": "VARCHAR",
            "IDProducto": "VARCHAR",
            "Cantidad": "INTEGER"
        }

class StockRegisterOut(StockRegisterCreate):
    __entity_name__ = "RegistroTransaccion"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)