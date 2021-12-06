from fastapi import HTTPException
import database
from datetime import datetime
import random
import string
from transaction_dto import Transaction


def generate_ref_number():
    return f"{random.choice(string.ascii_uppercase)}" \
           f"{random.choice(string.ascii_lowercase)}" \
           f"{random.choice(string.ascii_uppercase)}" \
           f"/{''.join([str(random.randint(1, 9)) for _ in range(12)])}"


def generate_currency_amount():
    return f"{random.choice(['$', '€', '¥'])}{random.randint(1, 1_000_000)}.{random.randint(0, 99)}"


def generate_transaction():
    return Transaction(
        date=datetime.utcnow(),
        amount=generate_currency_amount(),
        ref_number=generate_ref_number()
    )


def get_current_transaction_key(user_id):
    if user_id not in database.transactions:
        return 1
    return max(int(k) for k in database.transactions[user_id].keys()) + 1


def add_to_db(current_transaction, user_id):
    transaction_id = get_current_transaction_key(user_id)
    if user_id not in database.transactions:
        database.transactions[user_id] = {}

    database.transactions[user_id][transaction_id] = current_transaction
    return database.transactions[user_id]


def validate_user_id_transaction_id(user_id, transaction_id):
    if user_id not in database.transactions:
        raise HTTPException(status_code=404, detail="User not found")
    if transaction_id not in database.transactions[user_id]:
        raise HTTPException(status_code=404, detail="Transaction not found")
