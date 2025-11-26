from fastapi import APIRouter
from app.models.convert_model import ConvertRequest
from app.services.convert_service import convert_items

router = APIRouter()

@router.post("/convert")
def convert(data: ConvertRequest):
    result = convert_items(data.source, data.target, data.amount)
    if result is None:
        return {"error": "Item inválido"}
    return result
