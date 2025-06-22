import pandas as pd
import importacion as imp
import implementacion as decl

def procesado(base_ventas):
    def importacion():
        control1 = None #control Archivo 1
        excel_ventas = None
        control1, excel_ventas = imp.validacion()
        if(control1 == True):
            print(f"Importacion hecha")
            try:
                decl.importacion(excel_ventas, base_ventas)
                json_data = base_ventas.exportar_a_json()
            except Exception as e:
                print(f"Ocurrió un error: {e}")    
    #--------------------------------
    importacion()
