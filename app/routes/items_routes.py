from fastapi import APIRouter
from app.data.items_values import values

router = APIRouter()

@router.get("/items")
def get_items():
    return sorted(values.keys())
