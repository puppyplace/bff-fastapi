from pydantic import BaseModel

# classe do usuario
class User(BaseModel):
    email: str
    password: str