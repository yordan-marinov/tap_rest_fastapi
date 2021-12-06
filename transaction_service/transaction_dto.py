from pydantic import BaseModel
from datetime import datetime


class Transaction(BaseModel):
    date: datetime
    amount: str
    ref_number: str
