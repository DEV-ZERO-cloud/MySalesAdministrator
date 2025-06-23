import logging
from fastapi import APIRouter, Security, Query, HTTPException, status
from fastapi.responses import JSONResponse

from backend.app.services.inventory_management.core.auth import get_current_user
from backend.app.services.inventory_management.models.stock_register import StockRegisterCreate,StockRegisterOut
from backend.app.services.general.logic.universal_controller_instance import universal_controller as controller

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

router = APIRouter(prefix="/move", tags=["move"])

@router.get("/consultar", response_class=JSONResponse)
def consultar():
    """
    Mensaje de consulta de registros de traslados.
    """
    return JSONResponse(content={"message": "Consulta de usuarios habilitada."})

@router.get("/register", response_class=JSONResponse)
async def get_registers():
    """
    Devuelve todos los registros de traslados registrados.
    """
    registers = controller.read_all(StockRegisterOut)
    logger.info(f"[GET /registers] Número de registros de traslados encontrados: {len(registers) if registers else -1}")
    return JSONResponse(content= {"cantidad":len(registers), "usuarios": registers})

@router.get("/register", response_class=JSONResponse)
def usuario(
    id: int = Query(...),
    current_user: dict = Security(get_current_user, scopes=["system", "administrador"])
):
    """
    Devuelve un usuario por su ID.
    """
    unit_register = controller.get_by_column(StockRegisterOut, "ID", id)
    if unit_register:
        logger.info(f"[GET /register] Registros de traslados encontrado: {unit_register.ID}")
        return JSONResponse(content=unit_register.model_dump())
    else:
        logger.warning(f"[GET /register] No se encontró registros de traslados con id={id}")
        raise HTTPException(status_code=404, detail="Registros de traslados no encontrado")