def extraer_cantidad_productos(estado):
    numero = ""
    if not isinstance(estado, str):
        estado = str(estado)  # Convertir a cadena
    for i in estado:
        if i.isnumeric():
            numero +=i
    n_productos = int(numero) if numero else 0
    return n_productos+1