from pydantic import BaseModel, Field
from uuid import UUID


class ProductBase(BaseModel):
    name: str
    category: str


class ProductCreate(ProductBase):
    """ Properties to receive via API on creation """
    pass


class Product(ProductBase):
    """ Properties to return to client """
    id: UUID

    class Config:
        from_attributes = True