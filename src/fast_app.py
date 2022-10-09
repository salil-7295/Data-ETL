"""
The Fast API module for the calculator
"""

from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculator


class Input(BaseModel):
    method: str
    val1: int
    val2: int


app = FastAPI()


@app.post("/calculate")
def operation(user_input: Input):
    return calculator(user_input.method, user_input.val1, user_input.val2)



