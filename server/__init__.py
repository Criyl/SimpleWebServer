from fastapi import FastAPI
from pydantic import BaseModel

__version__ = '1.1.1'
app: FastAPI = FastAPI()


class ResponseContentModel(BaseModel):
    msg: str


@app.get("/")
def getHelloWorld() -> ResponseContentModel:
    return ResponseContentModel(msg="hello world")
