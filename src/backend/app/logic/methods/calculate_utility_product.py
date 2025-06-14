from logic.producto import Producto
from logic.venta import Venta

def calcular_utilidad(producto: Producto, venta: Venta):
    producto.ingresos_por_producto = float(producto.unidades * producto.precio_unitario_publicacion)
    
    if venta.ingresos_productos > 0:
        producto.porcentaje_influencia = producto.ingresos_por_producto / venta.ingresos_productos
    else:
        producto.porcentaje_influencia = 0.0
    
    producto.ingresos_por_envio = producto.porcentaje_influencia * venta.ingresos_envio
    producto.costo_envio = producto.porcentaje_influencia * venta.costos_envio
    producto.cargos_por_venta_impuestos = producto.porcentaje_influencia * venta.cargos
    producto.anulaciones_reembolsos = producto.porcentaje_influencia * venta.anulaciones

    producto.total = (
        producto.ingresos_por_producto +
        producto.ingresos_por_envio +
        producto.cargos_por_venta_impuestos +
        producto.costo_envio +
        producto.anulaciones_reembolsos
    )

    producto.utilidad_bruta = producto.total - (producto.costo_neto_unitario * producto.unidades)
