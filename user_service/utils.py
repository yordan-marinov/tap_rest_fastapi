import database
import urls
import models
import requests


def get_id():
    while True:
        response = requests.get(urls.ID_SERVICE)
        if response.ok:
            return response.json()


def get_address(user_id):
    url = f"{urls.ADDRESS_SERVICE_BASE}/generate/{user_id}"
    address = requests.get(url)

    return address.json()


def get_address_key(user_id):
    url = f"{urls.ADDRESS_SERVICE_BASE}/key/{user_id}"

    return requests.get(url).text


def get_transaction_key(user_id):
    url = f"{urls.TRANSACTION_SERVICE_BASE}/key/{user_id}"

    return requests.get(url).text


def make_transaction(user_id):
    url = f"{urls.TRANSACTION_SERVICE_BASE}/generate/{user_id}"
    transaction = requests.get(url)

    return transaction.json()


def add_to_db(user):
    user_key = user.user_id
    if user_key not in database.user_db:
        database.user_db[user_key] = {}

    database.user_db[user_key] = user
    return database.user_db[user_key]


def generate_user(user_name):
    user_id = get_id().get("id")
    return models.User(
        user_id=user_id,
        first_name=user_name.first_name,
        last_name=user_name.last_name,
        addresses=get_address(user_id),
        transactions=make_transaction(user_id)
    )


def create_user(user_id, user_name, address):
    address_key = get_address_key(user_id)
    new_address = {address_key: address}
    # transaction_key = get_transaction_key(user_id)
    # new_transaction = {transaction_key: make_transaction(user_id)}
    return models.User(
        user_id=get_id().get("id"),
        first_name=user_name.first_name,
        last_name=user_name.last_name,
        addresses=new_address,
        transactions=make_transaction(user_id)
    )
