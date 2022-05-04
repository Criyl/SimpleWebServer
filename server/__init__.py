from fastapi import FastAPI
from pydantic import BaseModel

__version__ = '1.1.0'
app: FastAPI = FastAPI()


class ResponseContentModel(BaseModel):
    msg: str


@app.get("/")
def getHelloWorld() -> ResponseContentModel:
    # fix some bug
    return ResponseContentModel(msg="hello world")
