"""
Name:       Mirza Haider
Email:      m.haiderbaig@gmail.com
LinkedIn:   https://www.linkedin.com/in/mirzahaiderbaig/

"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.routers import product, inventory, sale, revenue_analysis
from app.database import engine, Base
from app import deps
import app.initial_data as init


# Create db models (But use Alembic in production)
Base.metadata.create_all(bind=engine)


app = FastAPI()


# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/initial-data")
def populate_initial_data(db: Session = Depends(deps.get_db)):
    """
    Hit this endpoint to populate database with test data
    """
    init.populate_data(db)


app.include_router(product.router)
app.include_router(inventory.router)
app.include_router(sale.router)
app.include_router(revenue_analysis.router)
