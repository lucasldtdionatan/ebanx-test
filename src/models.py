from decimal import Decimal
from pydantic import BaseModel


class Event(BaseModel):
    type: str
    destination: str | None = None
    amount: Decimal
    origin: str | None = None
