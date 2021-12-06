from pydantic import BaseModel


class Address(BaseModel):
    street_number: int
    street_name: str
    city: str

