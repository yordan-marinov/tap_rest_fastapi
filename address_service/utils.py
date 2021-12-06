from fastapi import HTTPException
import database
import json
import random
from address_dto import Address


def generate_address():
    with open("data_src.json") as f:
        data_src = json.load(f)

    street_number = f"{random.randint(1, 100)}"
    street_name = f"{random.choice(data_src[1]['street'])} str."
    city = random.choice(data_src[0]['city'])

    return Address(
        street_number=street_number,
        street_name=street_name,
        city=city
    ).dict()


def get_current_address_key(user_id):
    if user_id not in database.addresses:
        return 1
    return max(int(k) for k in database.addresses[user_id].keys()) + 1


def add_to_database(current_address, user_id):
    address_id = get_current_address_key(user_id)
    if user_id not in database.addresses:
        database.addresses[user_id] = {}

    database.addresses[user_id][int(address_id)] = current_address


def validate_user_id_address_id(user_id, address_id):
    if user_id not in database.addresses:
        raise HTTPException(status_code=404, detail="User not found")
    if address_id not in database.addresses[user_id]:
        raise HTTPException(status_code=404, detail="Address not found")
