from pydantic import BaseModel
from uuid import UUID


class InventoryBase(BaseModel):
    product_id: UUID
    quantity: int
    reorder_threshold: int


class InventoryCreate(InventoryBase):
    """ Properties to receive via API on creation """
    pass


class Inventory(InventoryBase):
    """ Properties to return to client """
    id: UUID

    class Config:
        from_attributes = True