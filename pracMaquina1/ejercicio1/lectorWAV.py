import struct

def wav(ruta):
    with open (ruta, "rb") as wav:
        cabecera = wav.read(12)
        riff, size, wave = struct.unpack("<4sI4s", cabecera)
        retorno = False
        if riff == b"RIFF" and wave == b"WAVE":
            print(f"ChunID: {riff}, Size: {size}, Format: {wave}")
            retorno = True
    return retorno
        
if __name__ == "__main__": 
    print("Cargue un archivo en la carpeta e ingrese su nombre con la extensión")
    ruta = "pracMaquina1/ejercicio1/" + str(input())
    if not wav(ruta):
        print("El archivo cargado no es WAV")  