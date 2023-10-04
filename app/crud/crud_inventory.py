from uuid import UUID
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Inventory


class CRUDInventory(CRUDBase):
    
    def get_by_product(self, db: Session, product_id: UUID):
        """ Return inventory row with this product_id """
        return (
            db.query(Inventory)
            .filter(Inventory.product_id == product_id)
            .first()
        )

    def update_quantity(
        self, db: Session, db_obj: Inventory, delta_quantity: int
    ):
        """ Update only quanity of a product by adding delta_quantity to existing """
        db_obj.quantity += delta_quantity
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


inventory = CRUDInventory(Inventory)
