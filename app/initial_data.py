from datetime import datetime, timedelta
from sqlalchemy import text
from sqlalchemy.orm import Session

from app import models


# Create initial data for demo


def populate_data(db: Session):
    """ Wrapper function to populate SQL tables """
    insert_time_dimension(db)
    insert_transactional_data(db)


def insert_time_dimension(db: Session):
    """ Populate time dimension for a period of 25 years (2000-2025) """
    curr = datetime(year=2000, month=1, day=1)
    stop = datetime(year=2025, month=12, day=31)

    while curr < stop:
        row = models.TimeDimension(
            date = curr.date(),
            year = curr.year,
            month = curr.month,
            week = curr.strftime("%W"),
            day_of_month = curr.day,
            day_of_week = curr.weekday()
        )
        curr = curr + timedelta(days=1)
        db.add(row)
    db.commit()


def insert_transactional_data(db: Session):
    """ Populate Table product, inventory, sale """
    try:
        # Read SQL file
        with open("app/initial_data.sql", "r") as sql_file:
            sql_script = sql_file.read()

        # Execute SQL
        db.execute(text(sql_script))
        db.commit()

    except Exception as e:
        raise e
