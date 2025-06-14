from pydantic import BaseModel
class CustomerCreate(BaseModel):
    __entity_name__ = "Comprador"
    ID: int #CC
    name: str #Comprador
    address: str #Domicilio
    city: str   #Municipio
    country:str #Pais

    def to_dict(self):
        return self.model_dump()
        
    @classmethod
    def get_fields(cls) -> dict:
        return {
            "CC": "INTEGER PRIMARY KEY",
            "Domicilio": "VARCHAR",
            "Municipio": "VARCHAR",
            "Pais": "VARCHAR",
        }
class CustomerOut(CustomerCreate):
    __entity_name__ = "Comprador"

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)