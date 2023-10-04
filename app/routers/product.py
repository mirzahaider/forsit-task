from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import deps, schemas, crud


router = APIRouter(prefix='/product', tags=['product'])


@router.post("/", response_model=schemas.Product)
def create_product(
    obj_in: schemas.ProductCreate,
    db: Session = Depends(deps.get_db)
):
    """
    Add a new product
    """
    return crud.product.create(db, obj_in=obj_in)


@router.get("/", response_model=List[schemas.Product])
def read_products(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
):
    """
    Retrieve products 
    """
    return crud.product.get_multi(db, skip=skip, limit=limit)
