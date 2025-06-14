from methods.get_date import get_time, get_year
from logic.producto import Producto
from logic.info import PalabrasClaves

#-------------------------------------
class Venta:
    productos = list()
    id_venta = None
    estado = None
    fecha_venta = None
    paquete_productos = None
    ingresos_por_producto = None
    ingresos_por_envio = None
    cargos_por_venta_impuestos = None
    costos_envio = None
    anulaciones_reembolsos = None
    total = None
    mes_facturacion = None
    venta_publicidad = None
    procesado = None
    cantidad_productos = None

    def __init__(self, fila, h, conjunto_filas):
        try:
            self.id_venta = int(fila["# de venta"])
            self.estado = fila["Estado"]
            self.fecha_venta = get_time(fila["Fecha de venta"])
            self.paquete_productos = True if fila["Paquete de varios productos"] == "Sí" else False
            self.ingresos_por_producto = float(fila["Ingresos por productos (COP)"])
            self.ingresos_por_envio = float(fila["Ingresos por envío (COP)"])
            self.cargos_por_venta_impuestos = float(fila["Cargo por venta e impuestos"])
            self.costos_envio = float(fila["Costos de envío"])
            self.anulaciones_reembolsos = float(fila["Anulaciones y reembolsos (COP)"])
            self.total = float(fila["Total (COP)"])
            self.mes_facturacion = fila["Mes de facturación de tus cargos"]
            self.venta_publicidad = fila["Venta por publicidad"] == "Sí"
            self.procesado = True

            if self.estado in PalabrasClaves.palabras_clave_entregado:
                self.productos = [Producto(fila, get_year(fila["Fecha de venta"]))]
            else:
                self.productos = [
                    Producto(conjunto_filas.iloc[i], get_year(conjunto_filas.iloc[i]["Fecha de venta"]))
                    for i in range(1, h)
                ]

            self.cantidad_productos = len(self.productos)
        except ValueError:
            self.id_venta = 0
            print(f"Advertencia: El valor '# de venta' no es válido: {fila['# de venta']}")

    def to_dict(self):
        return {
            'id_venta': self.id_venta,
            'estado': self.estado,
            'fecha_venta': self.fecha_venta,
            'paquete_productos': self.paquete_productos,
            'ingresos totales': self.ingresos_por_producto,
            'ingresos_por_envio': self.ingresos_por_envio,
            'cargos_por_venta_impuestos': self.cargos_por_venta_impuestos,
            'costos_envio': self.costos_envio,
            'anulaciones_reembolsos': self.anulaciones_reembolsos,
            'total': self.total,
            'mes_facturacion': self.mes_facturacion,
            'venta_publicidad': self.venta_publicidad,
            "productos": [producto.to_dict() for producto in self.productos],
            'cantidad_productos': self.cantidad_productos,
            'procesado': self.procesado
        }

    @staticmethod
    def from_dict(data):
        venta = Venta.__new__(Venta)
        venta.id_venta = data['id_venta']
        venta.estado = data['estado']
        venta.fecha_venta = get_time(data['fecha_venta'])
        venta.paquete_productos = data['paquete_productos']
        venta.ingresos_por_producto = data['ingresos totales']
        venta.ingresos_por_envio = data['ingresos_por_envio']
        venta.cargos_por_venta_impuestos = data['cargos_por_venta_impuestos']
        venta.costos_envio = data['costos_envio']
        venta.anulaciones_reembolsos = data['anulaciones_reembolsos']
        venta.total = data['total']
        venta.mes_facturacion = data['mes_facturacion']
        venta.venta_publicidad = data['venta_publicidad']
        venta.productos = [Producto.from_dict(prod) for prod in data['productos']]
        venta.cantidad_productos = data['cantidad_productos']
        venta.procesado = data['procesado']
        return venta

    def calcular_utilidad(self, producto: Producto):
        try:
            producto.ingresos_por_producto = float(producto.unidades * producto.precio_unitario_publicacion)
            if self.ingresos_por_producto > 0:
                producto.porcentaje_influencia = producto.ingresos_por_producto / self.ingresos_por_producto
                producto.ingresos_por_envio = producto.porcentaje_influencia * self.ingresos_por_envio
                producto.costo_envio = producto.porcentaje_influencia * self.costos_envio
                producto.cargos_por_venta_impuestos = producto.porcentaje_influencia * self.cargos_por_venta_impuestos
                producto.anulaciones_reembolsos = producto.porcentaje_influencia * self.anulaciones_reembolsos
                producto.total = (
                    producto.ingresos_por_producto +
                    producto.ingresos_por_envio +
                    producto.cargos_por_venta_impuestos +
                    producto.costo_envio +
                    producto.anulaciones_reembolsos
                )
                producto.total = round(producto.total, 2)
                producto.utilidad_bruta = producto.total - (producto.costo_neto_unitario * producto.unidades)
            else:
                producto.porcentaje_influencia = 0.0
        except:
            producto.costo_neto_unitario = None
    def costeo(self):
        for producto in self.productos:
            self.calcular_utilidad(producto)

    def __str__(self):
        return f"#{self.id_venta} - {self.fecha_venta} - Total: {self.total} - Cantidad productos: {self.cantidad_productos}"
