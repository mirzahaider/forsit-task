from typing import Annotated
from fastapi import APIRouter, Depends, Query
from sqlalchemy import func
from sqlalchemy.orm import Session

from app import deps, models, schemas, crud
from app.models import Product, Sale, TimeDimension


router = APIRouter(prefix='/analysis', tags=['revenue analysis'])


@router.post("/")
def analyse(
    date_range: schemas.DateRange,

    dimension_1: Annotated[str, None, Query(
        description="Choose from daily, weekly, monthly, yearly"
    )] = "daily",

    dimension_2: Annotated[str, None, Query(
        description="Choose category or None"
    )] = None,

    db: Session = Depends(deps.get_db)
):
    # A dynamic list of required columns
    # Columns determined based on selected dimensions
    column_list = []

    if dimension_1 == "daily":
        column_list.append(TimeDimension.date)
    else:
        column_list.append(TimeDimension.year)
        if dimension_1 == "weekly":
            column_list.append(TimeDimension.week)
        elif dimension_1 == "monthly":
            column_list.append(TimeDimension.month)

    if dimension_2 == "category":
        column_list.append(Product.category)

    # Make query
    query = (
        db.query(
            *column_list,
            func.sum(Sale.quantity * Sale.unit_price).label("sales")
        )
        .join(Product, Product.id == Sale.product_id)
        .join(TimeDimension, TimeDimension.date == Sale.time_dimension)
        .filter(TimeDimension.date >= date_range.start_date)
        .filter(TimeDimension.date <= date_range.end_date)
        .group_by(*column_list)
        .order_by(*column_list)
    )

    # Get column names of query set & return accordingly
    result = query.all()
    cols = [c['name'] for c in query.column_descriptions]

    ret = []
    for row in result:
        d = {}
        for i in range(len(row)):
            d[cols[i]] = row[i]
        ret.append(d)

    return ret
