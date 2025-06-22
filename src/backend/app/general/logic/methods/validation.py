from ver2.methods.importation import lectura_archivos
def validacion():
    hoja_ventas, hoja_productos =lectura_archivos()
    if hoja_ventas is not None and hoja_productos is not None:
        return True, True,hoja_ventas, hoja_productos
    else:
        return False, False,None,None