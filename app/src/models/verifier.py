from pydantic import BaseModel

# classe para checar o idToken
class Verifier(BaseModel):
    idToken: str