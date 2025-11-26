from pydantic import BaseModel

class ConvertRequest(BaseModel):
    source: str
    target: str
    amount: float
