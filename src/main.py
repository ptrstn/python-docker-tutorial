from typing import Union

import debugpy
import redis
from fastapi import FastAPI

app = FastAPI()

r = redis.Redis(host="redis", port=6379)

debugpy.listen(("0.0.0.0", 5678))


@app.get("/")
def read_root():
    return {"Hello": "World!!!1"}


@app.get("/hits")
def hits():
    r.incr("hits")
    return {"number of hits": r.get("hits")}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
