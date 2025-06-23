import logging
from fastapi import Body, HTTPException, APIRouter, status
from fastapi.responses import JSONResponse

from backend.app.services.inventory_management.models.stock_register import StockRegisterCreate, StockRegisterOut
from backend.app.services.inventory_management.models.product_movements import ProductMovement
from backend.app.services.general.logic.universal_controller_instance import universal_controller as controller

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

router = APIRouter(prefix="/move", tags=["move"])

@router.get("/crear", response_class=JSONResponse)
def index_create():
    try:
        users = controller.read_all(StockRegisterOut)
        ultimo_id = max(p["ID"] for p in users) if users else 0
        nuevo_id = ultimo_id + 1
        return JSONResponse(
            content={
                "nuevo_id": nuevo_id,
            }
        )
    except Exception as e:
        logger.error(f"Error al obtener el último ID: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": f"Error al obtener el último ID: {str(e)}"}
        )

@router.post("/create-multi", response_class=JSONResponse)
async def create_multi_stock_register(
    data: StockRegisterCreate = Body(...)
):
    try:
        # 1. Guardar cabecera (StockRegister)
        stock_header = StockRegisterCreate(
            id=data.id,
            date=data.date,
            id_store_start=data.id_store_start,
            id_store_end=data.id_store_end,
            products=data.products
        )
        logger.info(f"Insertando cabecera de traslado: {stock_header.to_dict()}")
        controller.add(stock_header)

        # 2. Guardar cada producto como línea de movimiento
        for prod in data.products:
            product_movement_data = ProductMovement(
                movimiento_id=data.id,  # ForeignKey a la cabecera
                id_product=prod.id_product,
                quantity=prod.quantity
            )
            logger.info(f"Insertando producto en traslado: {product_movement_data.model_dump()}")
            controller.add(product_movement_data)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "operation": "create-multi",
                "success": True,
                "data": stock_header.to_dict(),
                "message": "Stock Register with multiple products created successfully."
            }
        )
    except ValueError as e:
        logger.warning(f"[POST /create-multi] Error de validación: {str(e)}")
        raise HTTPException(400, detail=str(e))
    except Exception as e:
        logger.error(f"[POST /create-multi] Error interno: {str(e)}")
        raise HTTPException(500, detail=f"Internal server error: {str(e)}")