def costear_producto(producto, año, costos_dict):
    id = producto.id_publicacion
    costo_neto_unitario = costos_dict.get(str(año), {}).get(id)

    if costo_neto_unitario is not None:
        return costo_neto_unitario  # Usar el valor que viene del JSON
    else:
        print(f" No se encontró costo neto para id {id} en el año {año}")
        return None