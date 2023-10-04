from sqlalchemy import Column, Integer, Date


from app.database import Base


class TimeDimension(Base):
    __tablename__ = "time_dimension"

    date = Column(Date, primary_key=True, index=True)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    week = Column(Integer, nullable=False)
    day_of_month = Column(Integer, nullable=False)
    day_of_week = Column(Integer, nullable=False)
