
from pydantic import BaseModel

class ClaseTitanic(BaseModel):
    Name: str
    Pclass: str
    Age: int
    Sex: str
    Survived: int

class ClaseTitanic1(BaseModel):
    Pclass: int
    Age: int
    Sex: int