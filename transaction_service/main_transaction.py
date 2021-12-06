from fastapi import FastAPI, HTTPException
import uvicorn
import utils
import database

app = FastAPI()


@app.get("/api/resource/transaction/generate/{user_id}")
async def generate_transactions(user_id: str):
    current_transaction = utils.generate_transaction()
    utils.add_to_db(current_transaction, user_id)

    return current_transaction


@app.get("/api/resource/transaction/all/{user_id}")
async def get_all(user_id: str):
    if user_id not in database.transactions:
        raise HTTPException(status_code=404, detail="Content not found")

    return database.transactions[user_id].items()


@app.get("/api/resource/transaction/one/{user_id}/{transaction_id}")
async def get_all(user_id: str, transaction_id: int):
    utils.validate_user_id_transaction_id(user_id, transaction_id)

    return database.transactions[user_id][transaction_id]


@app.get("api/resource/transaction/key/{user_id}")
async def get_transaction_key(user_id: str):
    return utils.get_current_transaction_key(user_id)


if __name__ == "__main__":
    uvicorn.run("main_transaction:app", host="127.0.0.1", port=8002)
