from Compresor import Compresor

if __name__ == "__main__":
    with open("archivo.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    Compresor(texto)