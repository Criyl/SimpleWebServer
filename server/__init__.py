from fastapi import FastAPI
from pydantic import BaseModel

__version__: str = '0.0.1'
app: FastAPI = FastAPI()


class Response(BaseModel):
    msg: str


@app.get("/")
def getHelloWorld() -> Response:
    return Response(msg="hello world")
