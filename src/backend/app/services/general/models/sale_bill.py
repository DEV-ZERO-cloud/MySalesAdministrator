from pydantic import BaseModel
class SaleBillCreate(BaseModel):
    __entity_name__ = "Venta_Factura"
    ID: int #ID
    date: str #Fecha
    state: str #Estado
    state_description: str   #Descripcion_Estado
    aremany: str   #VariosProductos (Si/No)
    units: int    #Unidades
    income_products: float  #IngresosProducto
    income_delivery: float  #IngresosEnvio
    cost_sale: float    #CargoVentas
    cost_delivery: float    #CostoEnvio
    refunds: float  #Anulaciones
    total: float    #Total
    billing_month: str  #MesFacturacion
    id_client: int  #IDComprador

    def to_dict(self):
        return self.model_dump()
        
    @classmethod
    def get_fields(cls) -> dict:
        return {
            "ID": "INTEGER PRIMARY KEY",
            "Fecha": "VARCHAR",
            "Estado": "VARCHAR",
            "Descripcion_Estado": "VARCHAR",
            "VariosProductos": "VARCHAR",
            "Unidades": "INTEGER",
            "IngresosProducto": "FLOAT",
            "IngresosEnvio": "FLOAT",
            "CargoVentas": "FLOAT",
            "CostoEnvio": "FLOAT",
            "Anulaciones": "FLOAT",
            "Total": "FLOAT",
            "MesFacturacion": "VARCHAR",
            "IDComprador": "INTEGER"
        }
class SaleBillOut(SaleBillCreate):
    __entity_name__ = "Venta_Factura"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)