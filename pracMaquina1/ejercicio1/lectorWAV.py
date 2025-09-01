#Se hace uso del módulo struct para desempaquetar los bytes leídos del archivo
import struct

def wav(ruta):
    with open (ruta, "rb") as wav:
        #Leemos los primeros 44 bytes debido a que ese es el tamaño de la cabecera
        cabecera = wav.read(44)
        #Desempaquetamos los primeros 12 bytes que corresponden al descriptor RIFF
        riff, chunkSize, format  = struct.unpack("@4sI4s", cabecera[0:12]) #4s: cadena de 4 bytes, I: entero sin signo (4 bytes)
        #Desempaquetamos los siguientes 24 bytes que corresponden al subchunk1 "fmt ", H: entero sin signo (2 bytes)
        subChunk1Id, subChunk1Size, audioFormat, numCh, sampleRate, byteRate, blockAlign, bitsPerSample = struct.unpack("@4sIHHIIHH", cabecera[12:36])
        #Desempaquetamos los últimos 8 bytes que corresponden al subchunk2 "data"
        subChunk2Id, subChunk2Size = struct.unpack("@4sI", cabecera[36:44]) 
        retorno = False
        if riff == b"RIFF" and subChunk1Id == b"fmt " and subChunk2Id == b"data":
            print("Cabecera del archivo WAV:\n")
            print(f"""Descriptor RIFF: 
                ChunkID: {riff}
                ChunkSize: {chunkSize}
                Format: {format}\n""")
            print(f"""Sub-Chunk fmt :
                Subchunk1ID: {subChunk1Id}
                Subchunk1Size: {subChunk1Size}
                AudioFormat: {audioFormat}
                NumChannels: {numCh}
                SampleRate: {sampleRate}
                ByteRate: {byteRate}
                BlockAlign: {blockAlign}
                BitsPerSample: {bitsPerSample}\n""")
            print(f"""Sub-Chunk data:
                Subchunk2ID: {subChunk2Id}
                Subchunk2Size: {subChunk2Size}\n""")
            retorno = True
    return retorno
        
if __name__ == "__main__": 
    print("Cargue un archivo en la carpeta e ingrese su nombre con la extensión")
    ruta = "pracMaquina1/ejercicio1/" + str(input())
    if not wav(ruta):
        print("El archivo cargado no es WAV")  