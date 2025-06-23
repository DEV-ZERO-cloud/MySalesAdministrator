import pandas as pd
import os
import json

class CostosDirectos:
    costos_dict = None
    def __init__(self, hoja: str, archivo: str):
        df = pd.read_excel(archivo, sheet_name=hoja, header=1)

        self.costos_dict = {}

        for _, row in df.iterrows():
            id_publicacion = str(row['# de publicación'])

            # Costo 2025
            costo_2025 = row['COSTO DIRTO']
            if not pd.isna(costo_2025):
                self.costos_dict.setdefault("2025", {})[id_publicacion] = costo_2025

            # Costo 2024
            costo_2024 = row['COSTO DIRTO.1']
            if not pd.isna(costo_2024):
                self.costos_dict.setdefault("2024", {})[id_publicacion] = costo_2024

        # Exportar a JSON
        with open(os.getenv("DIR_COSTOS_HISTORICOS"), "w", encoding="utf-8") as f:
            json.dump(self.costos_dict, f, indent=4, ensure_ascii=False)

        print("Exportación completa desde hoja:", hoja)
