import datetime
import random
import uuid

import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/info/generate/id")
async def generate_id():
    rand_int = random.Random().randint(0, 10000)

    if rand_int >= 5121:
        return {"dateOfExecution": datetime.datetime.utcnow(), "id": uuid.uuid4()}
    elif rand_int <= 5121:
        raise HTTPException(status_code=500, detail="connection failed")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
