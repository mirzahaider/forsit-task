from pydantic import BaseModel
from datetime import datetime, date
from uuid import UUID


class SaleBase(BaseModel):
    product_id: UUID
    quantity: int
    unit_price: float


class SaleCreate(SaleBase):
    """ Properties to receive via API on creation """
    pass


class Sale(SaleBase):
    """ Properties to return to client """
    id: UUID
    datetime: datetime
    time_dimension: date
    
    class Config:
        from_attributes = True
