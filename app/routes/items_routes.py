from fastapi import APIRouter
from app.data.items_values import values

router = APIRouter()

@router.get("/items", tags=["Items"], summary="Lista todos los items tradeables", description="Devuelve una lista completa de todos los ítems que soporta el sistema: minerales, alimentos, estaciones de trabajo, etc.")
def get_items():
    return sorted(values.keys())
