from pydantic import BaseModel
from datetime import date


class DateRange(BaseModel):
    start_date: date = '2020-01-01'
    end_date: date = '2024-01-01'
