from Compresor import compresor
from Descompresor import descomprimir
import json

def cargar_datos(archivo_salida="comprimido.txt"):
    with open(archivo_salida, "r", encoding="utf-8") as f: # Abrimos el archivo y cargamos el contenido JSON
        datos = json.load(f)
    return datos["codigosAscii"], datos["arboles"], datos["comprimido"] # Devolvemos los tres elementos necesarios


if __name__ == "__main__":
    with open("HuffmanMO2/archivo.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    compresor(texto)
    codAscii, arboles, comprimido = cargar_datos("HuffmanMO2/comprimido.txt")
    descomprimir(comprimido, arboles, codAscii)
