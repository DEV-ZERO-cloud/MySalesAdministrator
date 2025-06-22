from logic.costos_directo import CostosDirectos
import json
class Producto:
    def __init__(self, fila, anio:str):
        try:
            self.id_producto = fila["# de publicación"]
            self.paquete_productos = True if fila["Paquete de varios productos"] == "Sí" else False
            self.unidades = float(fila["Unidades"])
            self.ingresos_por_producto = float(fila['Ingresos por productos (COP)'])
            self.ingresos_por_envio = float(fila['Ingresos por envío (COP)'])
            self.total = float(fila['Total (COP)'])
            self.cargos_por_venta_impuestos = float(fila['Cargo por venta e impuestos'])
            self.costo_envio =float(fila['Costos de envío'])
            self.precio_unitario_publicacion = float(fila["Precio unitario de venta de la publicación (COP)"])
            self.anulaciones_reembolsos = float(fila["Anulaciones y reembolsos (COP)"])
            self.costo_neto_unitario = self.costear_producto(anio)
            self.porcentaje_influencia =float(0)
            self.utilidad_bruta =float(0)
            self.SKU = fila["SKU"]
            self.id_publicacion = fila["# de publicación"]
            self.titulo_publicacion = fila["Título de la publicación"]
            self.procesado = True
        except ValueError:
            print(f"Advertencia: El valor '# de publicación' no es válido: {fila['# de publicación']}")

    def costear_producto(self, año):
        with open("./ver2/storage/costos_historicos.json", "r", encoding="utf-8") as f:
            costos_dict = json.load(f)
            
        id = self.id_producto
        costo_neto_unitario = costos_dict.get(str(año), {}).get(id)

        if costo_neto_unitario is not None:
            return costo_neto_unitario  # Usar el valor que viene del JSON

        else:
            print(f"No se encontró costo neto para id {id} en el año {año}")
            return None
    def to_dict(self):
        # Retorna los atributos de la clase como un diccionario
        return {
            'id_producto': self.id_producto,
            'paquete_productos': self.paquete_productos,
            'unidades': self.unidades,
            'Porcentaje de influencia en la venta': self.porcentaje_influencia,
            'ingresos_por_producto': self.ingresos_por_producto,
            'ingresos_por_envio': self.ingresos_por_envio,
            'cargos_por_venta_impuestos': self.cargos_por_venta_impuestos,
            'costo_por_envio':self.costo_envio,
            'anulaciones_reembolsos':self.anulaciones_reembolsos,
            'total':self.total,
            'costo neto unitario': self.costo_neto_unitario,
            'utilidad bruta': self.utilidad_bruta,
            'SKU': self.SKU,
            'id_publicacion': self.id_producto,
            'titulo_publicacion': self.titulo_publicacion,
            'precio_unitario_publicacion': self.precio_unitario_publicacion,
            'procesado': self.procesado
        }
    @staticmethod
    def from_dict(data):
        # Reconstruye una instancia de Producto a partir de un diccionario
        producto = Producto.__new__(Producto)  # Crear instancia sin llamar a __init__
        producto.id_producto = data['id_producto']
        producto.paquete_productos = data['paquete_productos']
        producto.unidades = data['unidades']
        producto.porcentaje_influencia = data['Porcentaje de influencia en la venta']
        producto.precio_unitario_publicacion = data['precio_unitario_publicacion']
        producto.ingresos_por_producto = data['ingresos_por_producto']
        producto.ingresos_por_envio = data['ingresos_por_envio']
        producto.cargos_por_venta_impuestos = data['cargos_por_venta_impuestos']
        producto.costo_envio = data['costos_por_envio']
        producto.anulaciones_reembolsos = data['anulaciones_reembolsos']
        producto.precio_unitario_publicacion = data['precio_unitario_publicacion']
        producto.costo_neto_unitario = data['costo neto unitario']
        producto.utilidad_bruta = data['utilidad bruta']
        producto.total = data['total']
        producto.SKU = data['SKU']
        producto.id_publicacion = data['id_publicacion']
        producto.titulo_publicacion = data['titulo_publicacion']
        producto.procesado = data['procesado']
        return producto