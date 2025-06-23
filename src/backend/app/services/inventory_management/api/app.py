import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.app.services.inventory_management.core.config import settings
from backend.app.services.inventory_management.core.middlewares import add_middlewares
from backend.app.services.general.logic.universal_controller_instance import universal_controller
from backend.app.services.inventory_management.api.routes

# Inicializar la aplicación FastAPI
app = FastAPI(title=settings.PROJECT_NAME)

# Añadir middlewares globales
add_middlewares(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:49607",  # solo si aún pruebas en local
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar archivos estáticos
static_dir = os.path.join(os.path.dirname(__file__), "../../../frontend/static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Eventos de inicio y apagado
@app.on_event("startup")
async def startup_event():
    print("Conexión establecida con la base de datos")

@app.on_event("shutdown")
async def shutdown_event():
    if universal_controller.conn:
        universal_controller.conn.close()
        print("Conexión cerrada correctamente")

# Incluir rutas de los microservicios
app.include_router("")