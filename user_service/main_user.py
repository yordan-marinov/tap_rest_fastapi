from fastapi import FastAPI
import uvicorn
import models
import database
import utils

app = FastAPI()


@app.post(f"/api/resource/create/user")
async def create_user_with_address(user_name: models.UserName, address: models.Address, ):
    user_id = utils.get_id().get("id")
    current_user = utils.create_user(user_id, user_name, address)
    utils.add_to_db(current_user)

    return database.user_db[current_user.user_id]


@app.post(f"/api/resource/generate/user")
async def generate_user(user_name: models.UserName):
    current_user = utils.generate_user(user_name)
    utils.add_to_db(current_user)

    return database.user_db[current_user.user_id]


@app.get("/api/resource/users")
async def get_all():
    return database.user_db


@app.get("/api/resource/user/{user_id}")
async def get_one_user(user_id: str, transactions_count: int):
    user = database.user_db[user_id]
    if transactions_count < len(user.transactions):
        transactions_count = len(user.transactions)

    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "id": user.user_id,
        "address": list(user.addresses.values()),
        "wanted_transactions": list(user.transactions.values())[:transactions_count]
    }


if __name__ == "__main__":
    uvicorn.run("main_user:app", host="127.0.0.1", port=8003)
