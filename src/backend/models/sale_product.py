from pydantic import BaseModel
class SaleBillCreate(BaseModel):
    __entity_name__ = "Venta_Producto"
    ID: int #IDVentaFactura
    IDProduct: int #IDProductoPublicacion
    units: int    #Unidades
    percentage: float   #PorcentajeInfluencia
    income_products: float  #IngresosProducto
    income_delivery: float  #IngresosEnvio
    cost_sale: float    #CargoVenta
    cost_delivery: float    #CostoEnvio
    refunds: float  #Anulaciones
    total: float    #Total

    def to_dict(self):
        return self.model_dump()
        
    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "IDProductoPublicacion": "INTEGER",
            "Unidades": "INTEGER",
            "IngresosProducto": "FLOAT",
            "IngresosEnvio": "FLOAT",
            "CargoVentas": "FLOAT",
            "CostoEnvio": "FLOAT",
            "Anulaciones": "FLOAT",
            "Total": "FLOAT",
        }
class SaleBillOut(SaleBillCreate):
    __entity_name__ = "Venta_Producto"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)