from logic.info import PalabrasClaves
from backend.logic.salestree import ArbolB_ventas
from logic.venta import Venta
from methods.get_amount_products import extraer_cantidad_productos
import pandas as pd

def get_b_tree(excel_ventas: pd.DataFrame, base_ventas: ArbolB_ventas):
    index = 0
    total_filas = len(excel_ventas)
    while index < total_filas:
        row = excel_ventas.iloc[index]

        if row.get("Procesado") == "Si":
            index += 1
            continue  # Salta filas ya procesadas

        estado = row.get("Estado", "").strip()

        if estado in PalabrasClaves.palabras_clave_entregado:
            # Venta de una sola fila
            venta = Venta(row, 1, row)
            base_ventas.insertar(venta)
            index += 1

        else:
            h = extraer_cantidad_productos(estado)

            if h > 1:
                if index + h <= total_filas:
                    conjunto_filas = excel_ventas.iloc[index:index+h]
                    venta = Venta(row, h, conjunto_filas)
                    base_ventas.insertar(venta)
                    index += h
                else:
                    # Si no hay suficientes filas para agrupar, salta
                    print(f"Venta incompleta en fila {index}. Se esperaban {h} filas.")
                    index += 1
            else:
                index += 1
