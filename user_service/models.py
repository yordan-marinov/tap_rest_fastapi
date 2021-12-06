from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    first_name: str
    last_name: str
    addresses: dict
    transactions: dict


class UserId(BaseModel):
    date: str
    user_id: str


class UserName(BaseModel):
    first_name: str
    last_name: str


class Address(BaseModel):
    street_number: int
    street_name: str
    city: str


class Transaction(BaseModel):
    transaction_id: int
    transactions: dict

# {"street_number": 99,"street_name": "Borova gora str.","city": "Plovdiv"}