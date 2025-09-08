import socket, subprocess

decodificacion = {
    "000": "A",
    "001": "B",
    "010": "C", 
    "011": "D",
    "100": "E",
    "101": "F",
    "110": "G",
    "111": "H"
}

#Decodificamos el mensaje
def decodificarMensaje(mensajeCodificado):
    bits = ""
    #Convertimos los bytes en una cadena de bits
    for byte in mensajeCodificado:
        #Concatenamos los bits de cada byte, usando format para convertir el byte en una cadena de 8 bits
        bits = bits + format(byte, '08b')
    #Tomamos 3 bits a la vez y los convertimos a su letra correspondiente
    mensajeDecodificado = ""
    for i in range(0, len(bits), 3):
        chunk = bits[i:i+3]
        mensajeDecodificado += decodificacion[chunk]
    return mensajeDecodificado
        
def servidor():
    ip = "0.0.0.0" 
    puerto = 5555 
    max_conexiones = 5 
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    servidor.bind((ip, puerto)) 
    servidor.listen(max_conexiones)
    print ("[*] Esperando conexiones en %s:%d" % (ip, puerto)) 
    cliente, direccion = servidor.accept()
    while True: 
        print ("[*] Conexion establecida con %s:%d" % (direccion[0] , direccion[1]))
        #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro la cantidad de bytes para recibir 
        recibido = cliente.recv(1024)
        #Si el mensaje recibido es vacío se cierra la aplicacion
        if not recibido: 
            print ("Adios.")
            break 
        #Mostramos los bytes recibidos
        print(str(direccion[0]) + " ha enviado (bytes): ", recibido)
        mensaje = decodificarMensaje(recibido)
        #Mostramos el mensaje decodificado 
        print (str(direccion[0]) + " dice: ", mensaje) 
        #Devolvemos el mensaje decodificado al cliente 
        cliente.send(mensaje.encode('utf-8')) 
        print ("Adios.") 
    #Cerramos la instancia del socket cliente y servidor 
    cliente.close() 
    servidor.close()

if __name__ == "__main__":
    servidor()