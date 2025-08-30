#Se hace uso del módulo struct para desempaquetar los bytes leídos del archivo
import struct

def wav(ruta):
    with open (ruta, "rb") as wav:
        #Leemos los primeros 12 bytes debido a que ese es el tamaño de la cabecera
        cabecera = wav.read(12)
        #Desempaquetamos los bytes leídos en 3 variables, el argumento "<4sI4s" indica que se leerán 3 valores,
        #el primero y el tercero son cadenas de 4 bytes y el segundo es un entero sin signo de 4 bytes
        riff, size, wave = struct.unpack("<4sI4s", cabecera)
        retorno = False
        #Si riff y wave son iguales a "RIFF" y "WAVE" respectivamente, entonces el archivo es un WAV
        if riff == b"RIFF" and wave == b"WAVE":
            print(f"ChunID: {riff}, Size: {size}, Format: {wave}")
            retorno = True
    return retorno
        
if __name__ == "__main__": 
    print("Cargue un archivo en la carpeta e ingrese su nombre con la extensión")
    ruta = "pracMaquina1/ejercicio1/" + str(input())
    if not wav(ruta):
        print("El archivo cargado no es WAV")  