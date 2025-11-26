from pydantic import BaseModel, Field

class ConvertRequest(BaseModel):
    source: str
    target: str
    amount: float


class ConversionPayload(BaseModel):
    source: str = Field(..., example="carrot", description="Item que tenés")
    target: str = Field(..., example="iron_ingot", description="Item que querés obtener")
    amount: float = Field(..., example=64, description="Cantidad disponible de item fuente")