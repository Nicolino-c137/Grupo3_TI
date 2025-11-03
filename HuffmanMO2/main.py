from Compresor import Compresor
from Descompresor import descomprimir
import json

def cargar_datos(archivo_salida="comprimido.txt"):
    with open(archivo_salida, "r", encoding="utf-8") as f:
        datos = json.load(f)
    return datos["codigosAscii"], datos["arboles"], datos["comprimido"]


if __name__ == "__main__":
    with open("archivo.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    Compresor(texto)
    codAscii, arboles, comprimido = cargar_datos("comprimido.txt")
    texto_recuperado = descomprimir(comprimido, arboles, codAscii)
    print("\nTexto descomprimido:", texto_recuperado)
