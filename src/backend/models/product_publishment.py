from pydantic import BaseModel
class ProductCostCreate(BaseModel):
    __entity_name__ = "Producto_Publicacion"
    ID: int #ID
    sales_channel: str #Canal_venta
    name: str #Titulo
    variant: str   #Variante
    unit_price: float   #Precio_unitario_venta
    publisment_type: str    #Tipo_publicacion

    def to_dict(self):
        return self.model_dump()
        
    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "Canal_venta": "VARCHAR",
            "Titulo": "VARCHAR",
            "Variante": "VARCHAR",
            "Precio_unitario_venta": "FLOAT",
            "Tipo_publicacion": "VARCHAR"
        }
class ProductCostOut(ProductCostCreate):
    __entity_name__ = "Producto_Publicacion"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)