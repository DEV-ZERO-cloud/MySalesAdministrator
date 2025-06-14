from datetime import datetime

def get_time(fecha_str: str):
    try:
        meses = {
            "enero": "01", "febrero": "02", "marzo": "03", "abril": "04",
            "mayo": "05", "junio": "06", "julio": "07", "agosto": "08",
            "septiembre": "09", "octubre": "10", "noviembre": "11", "diciembre": "12"
        }

        fecha_str = fecha_str.lower().replace("hs.", "").strip()
        partes = fecha_str.split()

        if len(partes) < 6:
            raise ValueError(f"Formato de fecha no reconocido: {fecha_str}")

        dia = partes[0].zfill(2)
        mes = meses.get(partes[2])
        anio = partes[4]
        hora = partes[5]

        if not mes:
            raise ValueError(f"Mes no reconocido: {partes[2]}")

        fecha_formateada = f"{anio}-{mes}-{dia} {hora}"
        return datetime.strptime(fecha_formateada, "%Y-%m-%d %H:%M")

    except Exception as e:
        print(f"Error al convertir fecha: {fecha_str} -> {e}")
        return None


def get_year(fecha_str: str):
    try:
        fecha_str = fecha_str.lower().replace("hs.", "").strip()
        partes = fecha_str.split()
        if len(partes) >= 5:
            return partes[4]
        else:
            raise ValueError("Formato de fecha inválido")
    except Exception as e:
        print(f"Error al extraer año de: {fecha_str} -> {e}")
        return None
