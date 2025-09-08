import socket 

codificacion = {
    "A": "000",
    "B": "001",
    "C": "010", 
    "D": "011",
    "E": "100",
    "F": "101",
    "G": "110",
    "H": "111"
}

#Codificamos el mensaje
def codificarMensaje(mensaje):
    mensajeCodificado = ""
    #Convertimos cada letra en su correspondiente cadena de 3 bits
    for ch in mensaje:
          mensajeCodificado += codificacion[ch]
    #Nos aseguramos que el mensaje tenga una longitud múltiplo de 8 bits
    while len(mensajeCodificado) % 8 != 0:
        mensajeCodificado += "0"    
    #Convertimos la cadena de bits en bytes, para esto sera necesario tomar 8 bits a la vez y convertirlos a su valor entero
    enteros = []
    for i in range(0, len(mensajeCodificado), 8):
        enteros.append(int(mensajeCodificado[i:i+8], 2))
    return bytes(enteros)

def cliente():
    #Servidor y Cliente se ejecutan en la misma máquina, conocida como localhost su dirección es 127.0.0.1 
    servidor = "127.0.0.1" 
    puerto = 5555 
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((servidor, puerto))
    mensaje = "AABBCCDDEEFFGGHH" #Cambiar por cualquier mensaje con letras de la A a la H
    data = codificarMensaje(mensaje)
    cliente.send(data)
    respuesta = cliente.recv(4096)
    print ("[*] Respuesta recibida: "+str(respuesta.decode()))
    cliente.close()

if __name__ == "__main__":
    cliente()