import struct, csv, os

#Guardamos los datos de las personas en una lista de diccionarios
def getDatos():
    personas = []
    ruta = os.getcwd()
    ruta = os.path.join(ruta, "Personas.csv")
    with open(ruta, "r", encoding="utf-8") as archi:
        lector_csv = csv.DictReader(archi)
        for fila in lector_csv:
            personas.append(fila)
    return personas

#Con esto empaquetamos los flags en un solo byte, si tenemos que un flag es "s" ponemos un 1 en la posicion correspondiente
def packFlags(*flags):
    byte = 0
    for i, flag in enumerate(flags):
        if flag == "s":
            byte |= (1 << i)
    return byte

#Con esto desempaquetamos los flags de un byte a una lista de 8 elementos
def unpackFlags(byte):
    flags = []
    for i in range(8):
        flags.append((byte >> i) & 1)
    return flags

#Escribimos los datos en un archivo binario con formato fijo
def guardarFijo(personas):
    #De esta forma decimos que apellido y nombre tiene 50 bytes, direccion 40, dni 8 y un byte para los flags
    formato = "50s40s8sB"
    ruta = os.getcwd()
    ruta = os.path.join(ruta, "fijos.dat")
    with open(ruta, "wb") as f:
        #Con ljust nos aseguramos que los strings tengan la longitud correcta, ya que estamos trabajando con un formato fijo
        for p in personas:
            apellidoYnombre = p["apellidoYnombre"].ljust(50)
            direccion = p["direccion"].ljust(40)
            dni = p["dni"].ljust(8)
            flags = packFlags(p["estudiosPrimarios"], p["estudiosSecundarios"], p["estudiosUniversitarios"], p["viviendaPropia"], p["obraSocial"], p["trabaja"], p["esJubilado"], p["tieneHijos"])
            #Codificamos los strings a bytes y los empaquetamos
            registro = struct.pack(formato, apellidoYnombre.encode("utf-8"), direccion.encode("utf-8"), dni.encode("utf-8"), flags)
            f.write(registro)

#Recuperamos los datos del archivo binario con formato fijo         
def leerFijo():
    personas = []
    formato = "50s40s8sB"
    ruta = os.getcwd()
    ruta = os.path.join(ruta, "fijos.dat")
    with open(ruta, "rb") as f:
        #Mientras podamos leer un chunk del tamaño del formato, lo desempaquetamos y lo agregamos a la lista
        while chunk := f.read(struct.calcsize(formato)):
            apellidoYnombre, direccion, dni, flags = struct.unpack(formato, chunk)
            #Con strip eliminamos los espacios en blanco que fueron agregados con ljust
            apellidoYnombre = apellidoYnombre.decode("utf-8").strip()
            direccion = direccion.decode("utf-8").strip()
            dni = dni.decode("utf-8").strip()
            flags = unpackFlags(flags)
            personas.append({
                "apellidoYnombre": apellidoYnombre,
                "direccion": direccion,
                "dni": dni,
                "estudiosPrimarios": "s" if flags[0] else "n",
                "estudiosSecundarios": "s" if flags[1] else "n",
                "estudiosUniversitarios": "s" if flags[2] else "n",
                "viviendaPropia": "s" if flags[3] else "n",
                "obraSocial": "s" if flags[4] else "n",
                "trabaja": "s" if flags[5] else "n",
                "esJubilado": "s" if flags[6] else "n",
                "tieneHijos": "s" if flags[7] else "n"
            })
    return personas
        
def listarPersonas(personas):
    for p in personas:
        print(f"""
Apellido y Nombre: {p["apellidoYnombre"]}
Direccion: {p["direccion"]}
DNI: {p["dni"]}
Estudios Primarios: {p["estudiosPrimarios"]}
Estudios Secundarios: {p["estudiosSecundarios"]}
Estudios Universitarios: {p["estudiosUniversitarios"]}
Vivienda Propia: {p["viviendaPropia"]}
Obra Social: {p["obraSocial"]}
Trabaja: {p["trabaja"]}
Es Jubilado: {p["esJubilado"]}
Tiene Hijos: {p["tieneHijos"]}
------------------------------""")

#Escribimos los datos en un archivo binario con formato variable
def guardarVariable(personas):
    ruta = os.getcwd()
    ruta = os.path.join(ruta, "variable.dat")
    with open(ruta, "wb") as f:
        for p in personas:
            apellidoYnombre = p["apellidoYnombre"].encode("utf-8")
            direccion = p["direccion"].encode("utf-8")
            dni = p["dni"].encode("utf-8")
            flags = packFlags(p["estudiosPrimarios"], p["estudiosSecundarios"], p["estudiosUniversitarios"], p["viviendaPropia"], p["obraSocial"], p["trabaja"], p["esJubilado"], p["tieneHijos"])
            #Guardamos la longitud de cada campo antes del campo en si
            registro = struct.pack("B", len(apellidoYnombre)) + apellidoYnombre
            registro += struct.pack("B", len(direccion)) + direccion
            registro += struct.pack("B", len(dni)) + dni
            registro += struct.pack("B", flags)
            f.write(registro)
          
#Recuperamos los datos del archivo binario con formato variable  
def leerVariable():
    personas = []
    ruta = os.getcwd()
    ruta = os.path.join(ruta, "variable.dat")
    with open(ruta, "rb") as f:
        while True:
            #Leemos el primer campo, si no hay nada mas que leer, salimos del bucle
            bof = f.read(1)
            if not bof:
                break
            #Desempaquetamos la longitud del campo y luego leemos el campo
            lenApellidoYnombre = struct.unpack("B", bof)[0]
            apellidoYnombre = f.read(lenApellidoYnombre).decode("utf-8")
            lenDireccion = struct.unpack("B", f.read(1))[0]
            direccion = f.read(lenDireccion).decode("utf-8")
            lenDni = struct.unpack("B", f.read(1))[0]
            dni = f.read(lenDni).decode("utf-8")
            flags = struct.unpack("B", f.read(1))[0]
            flags = unpackFlags(flags)
            personas.append({
                "apellidoYnombre": apellidoYnombre,
                "direccion": direccion,
                "dni": dni,
                "estudiosPrimarios": "s" if flags[0] else "n",
                "estudiosSecundarios": "s" if flags[1] else "n",
                "estudiosUniversitarios": "s" if flags[2] else "n",
                "viviendaPropia": "s" if flags[3] else "n",
                "obraSocial": "s" if flags[4] else "n",
                "trabaja": "s" if flags[5] else "n",
                "esJubilado": "s" if flags[6] else "n",
                "tieneHijos": "s" if flags[7] else "n"
            })
    return personas
            

if __name__ == "__main__":
    personas = getDatos()
    guardarFijo(personas)
    datos = leerFijo()
    #listarPersonas(datos) #Descomentar para ver los datos leidos del archivo binario
    guardarVariable(personas)
    datos = leerVariable()
    #listarPersonas(datos) #Descomentar para ver los datos leidos del archivo binario
    print("Comparamos el tamaño de los archivos:")
    print(f"Archivo con formato fijo: {os.path.getsize('pracMaquina1/ejercicio5/fijos.dat')} bytes")
    print(f"Archivo con formato variable: {os.path.getsize('pracMaquina1/ejercicio5/variable.dat')} bytes")