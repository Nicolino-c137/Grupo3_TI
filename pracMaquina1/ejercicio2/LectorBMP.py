#Uso de libreria struct para manejar archivos BMP
import struct

def mostrar_datos_cabecera(cabecera):
    # datos del BITMAPFILEHEADER (14 bytes)
    bfType = cabecera[0:2].decode("utf-8")       # "BM"
    bfSize = struct.unpack("<I", cabecera[2:6])[0]
    bfReserved1 = struct.unpack("<H", cabecera[6:8])[0]
    bfReserved2 = struct.unpack("<H", cabecera[8:10])[0]
    bfOffBits = struct.unpack("<I", cabecera[10:14])[0]
    # datos del BITMAPINFOHEADER (40 bytes)
    biSize = struct.unpack("<I", cabecera[14:18])[0]
    biWidth = struct.unpack("<I", cabecera[18:22])[0]
    biHeight = struct.unpack("<I", cabecera[22:26])[0]
    biPlanes = struct.unpack("<H", cabecera[26:28])[0]
    biBitCount = struct.unpack("<H", cabecera[28:30])[0]
    biCompression = struct.unpack("<I", cabecera[30:34])[0]
    biSizeImage = struct.unpack("<I", cabecera[34:38])[0]
    biXPelsPerMeter = struct.unpack("<I", cabecera[38:42])[0]
    biYPelsPerMeter = struct.unpack("<I", cabecera[42:46])[0]
    biClrUsed = struct.unpack("<I", cabecera[46:50])[0]
    biClrImportant = struct.unpack("<I", cabecera[50:54])[0]
    print("=== BITMAPFILEHEADER ===")
    print("Tipo:", bfType)
    print("Tamaño del archivo:", bfSize, "bytes")
    print("Reservado1:", bfReserved1)
    print("Reservado2:", bfReserved2)
    print("Offset datos:", bfOffBits, "bytes")
    print("\n=== BITMAPINFOHEADER ===")
    print("Tamaño cabecera:", biSize)
    print("Ancho:", biWidth, "px")
    print("Alto:", biHeight, "px")
    print("Planos:", biPlanes)
    print("Bits por pixel:", biBitCount)
    print("Compresión:", biCompression)
    print("Tamaño imagen:", biSizeImage, "bytes")
    print("Resolución X:", biXPelsPerMeter, "px/m")
    print("Resolución Y:", biYPelsPerMeter, "px/m")
    print("Colores usados:", biClrUsed)
    print("Colores importantes:", biClrImportant)


#Subprograma que verifica que el archivo sea BMP
def verificar_archivo(archivo):
    cabecera = archivo.read(54) #se leen los 54 correspondientes
    bfType = cabecera[0:2].decode("utf-8") #se decodifica los bytes que identifican el archivo
    if bfType=="BM":
        mostrar_datos_cabecera(cabecera)
    else:
        print("El archivo no tiene extension bmp")
    return
    
   
        
if __name__=='__main__':
    archivo= open("example.bmp","rb") #se abre el archivo 
    verificar_archivo(archivo)
    archivo.close() #se cierra el archivo



