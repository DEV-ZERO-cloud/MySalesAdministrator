import json
import os
from datetime import datetime, date
from logic.venta import Venta
from logic.info import PalabrasClaves
from methods.calculate_utility_product import calcular_utilidad


class CustomJSONEncoder(json.JSONEncoder):
    """Encoder personalizado para serializar objetos datetime y clases con to_dict."""
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if hasattr(obj, 'to_dict'):
            return obj.to_dict()
        if hasattr(obj, '__dict__'):
            return obj.__dict__
        return super().default(obj)


class NodoB:
    """Nodo de un árbol B para ventas."""
    def __init__(self, orden):
        self.claves = []      # Lista de tuplas (año, mes)
        self.hijos = []       # Hijos del nodo
        self.ventas = []      # Lista de ventas si es hoja
        self.es_hoja = True   # Indica si el nodo es hoja
        self.orden = orden    # Orden del árbol (máx. de claves)


class ArbolBVentas:
    """Árbol B para almacenamiento y gestión de ventas."""

    def __init__(self, orden):
        self.raiz = NodoB(orden)
        self.orden = orden

    def insertar(self, venta: Venta):
        """Inserta una venta en el árbol."""
        nodo = self.raiz
        if len(nodo.claves) == (2 * self.orden) - 1:
            nueva_raiz = NodoB(self.orden)
            nueva_raiz.es_hoja = False
            nueva_raiz.hijos.append(self.raiz)
            self._dividir_hijo(nueva_raiz, 0, self.raiz)
            self.raiz = nueva_raiz
            self._insertar_no_lleno(self.raiz, venta)
        else:
            self._insertar_no_lleno(nodo, venta)

    def _insertar_no_lleno(self, nodo, venta):
        clave = (venta.fecha_venta.year, venta.fecha_venta.month)
        i = len(nodo.claves) - 1

        if nodo.es_hoja:
            if clave in nodo.claves:
                idx = nodo.claves.index(clave)
                nodo.ventas[idx].append(venta)
            else:
                while i >= 0 and clave < nodo.claves[i]:
                    i -= 1
                nodo.claves.insert(i + 1, clave)
                nodo.ventas.insert(i + 1, [venta])
        else:
            while i >= 0 and clave < nodo.claves[i]:
                i -= 1
            i += 1
            if len(nodo.hijos[i].claves) == (2 * self.orden) - 1:
                self._dividir_hijo(nodo, i, nodo.hijos[i])
                if clave > nodo.claves[i]:
                    i += 1
            self._insertar_no_lleno(nodo.hijos[i], venta)

    def _dividir_hijo(self, padre, indice, hijo):
        nuevo_hijo = NodoB(self.orden)
        nuevo_hijo.es_hoja = hijo.es_hoja
        padre.claves.insert(indice, hijo.claves[self.orden - 1])
        padre.hijos.insert(indice + 1, nuevo_hijo)
        nuevo_hijo.claves = hijo.claves[self.orden:]
        hijo.claves = hijo.claves[:self.orden - 1]

        if hijo.es_hoja:
            nuevo_hijo.ventas = hijo.ventas[self.orden:]
            hijo.ventas = hijo.ventas[:self.orden]
        else:
            nuevo_hijo.hijos = hijo.hijos[self.orden:]
            hijo.hijos = hijo.hijos[:self.orden]

    def buscar(self, anio, mes, id_venta=None):
        """Busca ventas por año, mes y opcionalmente por id de venta."""
        ventas = self._buscar_en_nodo(self.raiz, [anio, mes])
        if ventas:
            if id_venta is not None:
                for venta in ventas:
                    if venta.id_venta == id_venta:
                        print("Venta encontrada")
                        return venta
                print(f"No se encontró la venta con ID {id_venta} en [{anio}, {mes}]")
                return None
            print(f"Ventas encontradas para ({anio}, {mes}): {ventas}")
            return ventas
        print(f"No se encontraron ventas para [{anio}, {mes}]")
        return None

    def _buscar_en_nodo(self, nodo, clave):
        print(f"Buscando clave {clave} en nodo con claves: {nodo.claves}")
        i = 0
        while i < len(nodo.claves):
            if clave[0] > nodo.claves[i][0]:
                i += 1
            elif clave[0] == nodo.claves[i][0]:
                if clave[1] > nodo.claves[i][1]:
                    i += 1
                else:
                    break
            else:
                break

        if i < len(nodo.claves) and clave == nodo.claves[i]:
            if nodo.es_hoja:
                print(f"Clave encontrada en hoja: {clave}")
                return nodo.ventas[i]
            return self._buscar_en_nodo(nodo.hijos[i], clave)
        elif nodo.es_hoja:
            print(f"Clave {clave} no encontrada en nodo hoja.")
            return None
        return self._buscar_en_nodo(nodo.hijos[i], clave)

    def buscar_y_imprimir(self, anio, mes, id_venta=None):
        """Busca e imprime ventas por año, mes y opcionalmente id."""
        ventas = self.buscar(anio, mes, id_venta)
        if not ventas:
            print(f"No se encontraron ventas para la clave [{anio}, {mes}].")
            return
        if id_venta is not None:
            print(f"Venta con ID {id_venta}:")
            print(ventas.to_dict())
        else:
            print(f"Ventas del periodo [{anio}, {mes}]:")
            for venta in ventas:
                print(venta.to_dict())

    def imprimir_arbol(self, nodo=None, nivel=0):
        """Imprime la estructura del árbol."""
        if nodo is None:
            nodo = self.raiz
        print(" " * nivel * 4 + str(nodo.claves))
        if not nodo.es_hoja:
            for hijo in nodo.hijos:
                self.imprimir_arbol(hijo, nivel + 1)

    def imprimir_hojas(self, nodo=None):
        """Imprime solo las hojas del árbol y sus ventas."""
        if nodo is None:
            nodo = self.raiz
        if nodo.es_hoja:
            print(f"Hojas: {nodo.claves} | Ventas: {nodo.ventas}")
        else:
            for hijo in nodo.hijos:
                self.imprimir_hojas(hijo)

    def exportar_a_json(self, archivo_json: str):
        """Exporta el árbol a un archivo JSON."""

        def nodo_a_dict(nodo):
            def convertir_venta(venta):
                return venta.to_dict()

            data = {
                "claves": nodo.claves,
                "ventas": [[convertir_venta(venta) for venta in lista_ventas] for lista_ventas in nodo.ventas] if nodo.es_hoja else None,
                "es_hoja": nodo.es_hoja
            }
            if not nodo.es_hoja:
                data["hijos"] = [nodo_a_dict(hijo) for hijo in nodo.hijos]
            return data

        if os.path.exists(archivo_json):
            with open(archivo_json, "r", encoding="utf-8") as archivo:
                try:
                    json.load(archivo)
                except json.JSONDecodeError:
                    print("El archivo existe pero está vacío o es inválido. Se sobrescribirá.")
        json_data = json.dumps(nodo_a_dict(self.raiz), indent=4, ensure_ascii=False, cls=CustomJSONEncoder)
        with open(archivo_json, "w", encoding="utf-8") as archivo:
            archivo.write(json_data)
        print(f"Exportación completada. Archivo guardado en: {archivo_json}")

    def importar_de_json(self, archivo_json: str):
        """Importa el árbol desde un archivo JSON."""

        def dict_a_nodo(data):
            nodo = NodoB(self.orden)
            nodo.claves = data["claves"]
            nodo.es_hoja = data["es_hoja"]
            if nodo.es_hoja:
                nodo.ventas = [
                    [Venta.from_dict(venta) for venta in lista_ventas]
                    for lista_ventas in data["ventas"]
                ]
            else:
                nodo.hijos = [dict_a_nodo(hijo) for hijo in data["hijos"]]
            return nodo

        try:
            with open(archivo_json, "r", encoding="utf-8") as archivo:
                datos_json = json.load(archivo)
            self.raiz = dict_a_nodo(datos_json)
            print(f"Importación completada desde el archivo: {archivo_json}")
        except FileNotFoundError:
            print(f"Error: El archivo {archivo_json} no existe.")
        except json.JSONDecodeError:
            print(f"Error: El archivo {archivo_json} no contiene un JSON válido.")

    def recorrer_y_costear(self, nodo=None):
        """Recorre el árbol y realiza el costeo de ventas."""
        if nodo is None:
            nodo = self.raiz
        if nodo.es_hoja:
            for clave, ventas in zip(nodo.claves, nodo.ventas):
                print(f"Clave (Año, Mes): {clave}")
                for venta in ventas:
                    venta.costeo()
        else:
            for i in range(len(nodo.claves)):
                self.recorrer_y_costear(nodo.hijos[i])
                print(f"Clave (Año, Mes): {nodo.claves[i]}")
            self.recorrer_y_costear(nodo.hijos[-1])

    @staticmethod
    def exportar_a_txt(arbol_ventas, archivo_txt):
        """Exporta el árbol a un archivo de texto plano tabulado."""
        with open(archivo_txt, mode='w', encoding='utf-8') as file:
            # Escribir encabezados
            file.write(
                '#_de_venta\tFecha_de_venta\tEstado\tUnidades\tIngresos_por_producto\tPorcentaje_de_influencia\t'
                'Ingresos_por_envio\tCargo_por_ventas_e_impuestos\tCostos_de_envio\tAnulaciones y Reembolsos\tTotal_(COP)\t'
                '#_de_publicacion\tTitulo_publicacion\tPrecio_Publicacion\tCosto_neto_unitario\tUtilidad_bruta\tMes_facturacion\n'
            )

            def recorrer_nodos(nodo):
                if nodo.es_hoja:
                    for i, clave in enumerate(nodo.claves):
                        for venta in nodo.ventas[i]:
                            if venta.estado in PalabrasClaves.palabras_clave_entregado:
                                file.write(
                                    f"{venta.id_venta}\t{venta.fecha_venta}\t{venta.estado}\t{venta.productos[0].unidades}\t{venta.ingresos_por_producto}\t1\t"
                                    f"{venta.ingresos_por_envio}\t{venta.cargos_por_venta_impuestos}\t{venta.costos_envio}\t{venta.anulaciones_reembolsos}\t{venta.total}\t"
                                    f"{venta.productos[0].id_publicacion}\t{venta.productos[0].titulo_publicacion}\t{venta.productos[0].precio_unitario_publicacion}\t{venta.productos[0].costo_neto_unitario}\t{venta.productos[0].utilidad_bruta}\t{venta.mes_facturacion}\n"
                                )
                            else:
                                file.write(
                                    f"{venta.id_venta}\t{venta.fecha_venta}\t{venta.estado}\t \t{venta.ingresos_por_producto}\t1\t"
                                    f"{venta.ingresos_por_envio}\t{venta.cargos_por_venta_impuestos}\t{venta.costos_envio}\t{venta.anulaciones_reembolsos}\t{venta.total}\t"
                                    f" \t \t \t \t \t{venta.mes_facturacion}\n"
                                )
                                for producto in venta.productos:
                                    file.write(
                                        f"{venta.id_venta}\t{venta.fecha_venta}\t{venta.estado}\t{producto.unidades}\t{producto.ingresos_por_producto}\t{producto.porcentaje_influencia}\t"
                                        f"{producto.ingresos_por_envio}\t{producto.cargos_por_venta_impuestos}\t{producto.costo_envio}\t{producto.anulaciones_reembolsos}\t{producto.total}\t"
                                        f"{producto.id_publicacion}\t{producto.titulo_publicacion}\t{producto.precio_unitario_publicacion}\t{producto.costo_neto_unitario}\t{producto.utilidad_bruta}\t{venta.mes_facturacion}\n"
                                    )
                else:
                    for i in range(len(nodo.claves)):
                        recorrer_nodos(nodo.hijos[i])

            recorrer_nodos(arbol_ventas.raiz)
            print(f"Datos exportados a {archivo_txt}")