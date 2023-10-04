from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID, ForeignKey("product.id"))
    quantity = Column(Integer, nullable=False)
    reorder_threshold = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="inventory")
