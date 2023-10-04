from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import deps, schemas, crud


router = APIRouter(prefix='/inventory', tags=['inventory'])


@router.post("/", response_model=schemas.Inventory)
def purchase_inventory(
    obj_in: schemas.InventoryCreate,
    db: Session = Depends(deps.get_db)
):
    """
    Add a product to inventory
    """
    product_id = obj_in.product_id

    # Product must exist in Product table
    if crud.product.get(db, id=product_id) is None:
        raise HTTPException(status_code=404, detail="Product not found")

    # If product already in inventory, update & add quantity
    db_obj = crud.inventory.get_by_product(db, product_id=product_id)
    if db_obj:
        # Set new quantity
        obj_in.quantity += db_obj.quantity
        return crud.inventory.update(db, db_obj=db_obj, obj_in=obj_in)

    # Else create entry for new inventory product
    return crud.inventory.create(db, obj_in=obj_in)


@router.get("/", response_model=List[schemas.Inventory])
def read_inventory(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve inventory 
    """
    return crud.inventory.get_multi(db, skip=skip, limit=limit)
