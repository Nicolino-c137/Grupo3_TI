from Compresor import compresor
from Descompresor import descomprimir

if __name__ == "__main__":
    with open("prueba.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    compresor(texto)
    descomprimir()