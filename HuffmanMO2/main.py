from Compresor import compresor
from Descompresor import descomprimir
import os

if __name__ == "__main__":
    ruta = os.getcwd()
    ruta = os.path.join(ruta, "HuffmanMO2/prueba.txt")
    with open(ruta, "r", encoding="utf-8") as f:
        texto = f.read()
    compresor(texto)
    descomprimir()