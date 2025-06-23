from pydantic import BaseModel

class ProductMovement(BaseModel):
    id: int  # opcional, si quieres llave primaria
    movimiento_id: int  # ForeignKey a StockRegister
    id_product: str
    quantity: int

    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "MovimientoID": "INTEGER",
            "IDProducto": "VARCHAR",
            "Cantidad": "INTEGER"
        }