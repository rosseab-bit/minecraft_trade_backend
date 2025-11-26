from fastapi import FastAPI
from app.routes import items_routes, convert_routes

app = FastAPI()

# Registrar rutas
app.include_router(items_routes.router)
app.include_router(convert_routes.router)

@app.get("/")
def root():
    return {"message": "Minecraft Trade API funcionando!"}
