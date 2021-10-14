from pydantic import BaseModel

class UserIdentify(BaseModel):
    email: str

# classe do usuario
class User(UserIdentify):
    password: str
