from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import deps, schemas, crud


router = APIRouter(prefix='/sales', tags=['sales'])


@router.post("/", response_model=schemas.Sale)
def create_sale(
    obj_in: schemas.SaleCreate,
    db: Session = Depends(deps.get_db)
):
    """
    Sell a product from inventory
    """

    # Product must exist in inventory
    inventory_product = crud.inventory.get_by_product(
        db, 
        product_id=obj_in.product_id
    )
    if inventory_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Stock quantity must be greater than sale quantity
    if inventory_product.quantity < obj_in.quantity:
        raise HTTPException(status_code=400, detail="Not enough quantity")
    
    # Update inventory
    crud.inventory.update_quantity(
        db, 
        db_obj=inventory_product, 
        delta_quantity=obj_in.quantity*(-1)
    )
    # Record sale
    return crud.sale.create(db, obj_in=obj_in)


@router.get("/", response_model=List[schemas.Sale])
def read_sales(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve Sales 
    """
    return crud.sale.get_multi(db, skip=skip, limit=limit)
