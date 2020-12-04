from pydantic import BaseModel

"""definición de los modelos de estado:"""

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str
    balance: int