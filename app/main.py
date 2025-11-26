from fastapi import FastAPI
from app.routes import items_routes, convert_routes

app = FastAPI(title="Minecraft Trade API",
    description="""
API para convertir ítems, minerales, alimentos y materiales de Minecraft  
en base al valor de 1 diamante.

Permite:
- Consultar valores relativos
- Convertir ítems entre sí
- Manejar estaciones de trabajo, alimentos y materiales
""",
    version="1.0.0",
    contact={
        "name": "Ricardo",
        "email": "roseab.developer@gmail.com",
    })

# Registrar rutas
app.include_router(items_routes.router)
app.include_router(convert_routes.router)

@app.get("/")
def root():
    return {"message": "Minecraft Trade API funcionando!"}
