import pandas as pd
#retorna un dataframe
def lectura_archivos():
    ruta_archivo1 = './ver2/docs/HOJA_VENTAS.xlsm'  # Ruta actual del archivo

    try:
        print(f"Leyendo archivo: {ruta_archivo1}...")
        df = pd.read_excel(ruta_archivo1, sheet_name=0, usecols='A:W', engine='openpyxl')
        # Diccionario de columnas con valores por defecto a rellenar
        columnas_a_rellenar = {
            'Total (COP)': 0,
            'Unidades': 0,
            'Fecha de venta': '01 de enero de 1970 00:00',
            'Ingresos por envío (COP)': 0,
            'Ingresos por productos (COP)': 0,
            'Cargo por venta e impuestos': 0,
            'Costos de envío': 0,
            'Anulaciones y reembolsos (COP)': 0,
            'Mes de facturación de tus cargos': 'NA',
            'Precio unitario de venta de la publicación (COP)': 0,
            'Variante': 'NA'
        }

        for columna, valor in columnas_a_rellenar.items():
            if columna in df.columns:
                df[columna] = df[columna].fillna(valor)
            else:
                print(f"La columna '{columna}' no fue encontrada en el archivo.")
        print("Lectura, limpieza y conversión de fechas completadas.")
        return df

    except Exception as e:
        print(f" Ocurrió un error al leer el archivo: {e}")
        return None