from fastapi import APIRouter, Body
from app.models.convert_model import ConvertRequest, ConversionPayload
from app.services.convert_service import convert_items

router = APIRouter()

@router.post("/convert", tags=["Conversion"], summary="Convierte un item a otro", description="Convierte un item fuente a un item destino basado en el valor relativo a 1 diamante.")
async def convert(data: ConvertRequest, payload: ConversionPayload = Body(
        ...,
        openapi_examples={
            "CarrotToIron": {
                "summary": "Convertir zanahorias a hierro",
                "value": {
                    "source": "carrot",
                    "target": "iron_ingot",
                    "amount": 64
                }
            },
            "WheatToDiamond": {
                "summary": "Convertir trigo a diamantes",
                "value": {
                    "source": "wheat",
                    "target": "diamond",
                    "amount": 128
                }
            }
        }
    )):
    result = convert_items(data.source, data.target, data.amount)
    if result is None:
        return {"error": "Item inválido"}
    return result
