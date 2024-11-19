# pydantic - data validation library
from pydantic import BaseModel

# by inheriting BaseModel, it becomes an Pydantic model which provide structure, validation and error handling
class KilometersRequest(BaseModel):
    target: int
    kilometers: int