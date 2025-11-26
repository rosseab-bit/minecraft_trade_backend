from fastapi import APIRouter
from app.models.convert_model import ConvertRequest
from app.services.convert_service import convert_items

router = APIRouter()

@router.post("/convert", tags=["Conversion"], summary="Convierte un item a otro", description="Convierte un item fuente a un item destino basado en el valor relativo a 1 diamante.")
def convert(data: ConvertRequest):
    result = convert_items(data.source, data.target, data.amount)
    if result is None:
        return {"error": "Item inválido"}
    return result
