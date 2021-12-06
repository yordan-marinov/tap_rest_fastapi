from fastapi import FastAPI, HTTPException
from address_dto import Address
import uvicorn
import database
import utils

app = FastAPI()


@app.post("/api/resource/address/add/{user_id")
async def add_address(user_id: str, address: Address):
    utils.add_to_database(address, user_id)

    return address


@app.post("/api/resource/address/generate/{user_id}")
async def generate_address(user_id: str):
    address = utils.generate_address()
    utils.add_to_database(address, user_id)

    return address


@app.get("/api/resource/address/all/{user_id}")
async def get_all(user_id: str):
    if user_id not in database.addresses:
        raise HTTPException(status_code=404, detail="Content not found")

    return database.addresses[user_id]


@app.get("/api/resource/address/{user_id}/one/{address_id}")
async def get_one(user_id: str, address_id: int):
    utils.validate_user_id_address_id(user_id, address_id)

    return database.addresses[user_id][address_id]


@app.delete("/api/resource/address/{user_id}/delete/{address_id}")
async def delete_address(user_id: str, address_id: int):
    utils.validate_user_id_address_id(user_id, address_id)
    del database.addresses[user_id][address_id]

    return database.addresses[user_id]


@app.put("/api/resource/address/{user_id}/update/{address_id}", response_model=Address)
async def update_address(user_id: str, address_id: int, address: Address):
    utils.validate_user_id_address_id(user_id, address_id)
    database.addresses[user_id][address_id].update(address)

    return database.addresses[user_id][address_id]


@app.get("/api/resource/address/key/{user_id}")
async def get_address_key(user_id: str):
    return utils.get_current_address_key(user_id)


if __name__ == "__main__":
    uvicorn.run("main_address:app", host="127.0.0.1", port=8001)
