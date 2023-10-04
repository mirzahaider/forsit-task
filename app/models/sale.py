from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, Float, func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.database import Base


class Sale(Base):
    __tablename__ = "sale"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID, ForeignKey("product.id"))
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    datetime = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    time_dimension = Column(Date, ForeignKey("time_dimension.date"), server_default=func.now())
