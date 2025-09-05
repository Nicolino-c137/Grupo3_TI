#Se utilzo las librerias csv para manipular la base de datos y os para obtener el tamaño del archivo
import csv
import os

#subprograma que se encarga de dar el formato correcto de los registros, es decir, los rellena con caracteres en blanco para cumplir con el tamaño
def formatear_registro(apellido_nombre, direccion, dni, estudios_primarios, estudios_secundarios, estudios_universitarios, vivienda_propia, obra_social, trabaja, es_jubilado, tiene_hijos):
    ayn=apellido_nombre.ljust(20)
    d=direccion.ljust(30)
    d_n_i=dni.ljust(8)
    e_p=estudios_primarios
    e_s=estudios_secundarios
    e_u=estudios_universitarios
    v_p=vivienda_propia
    o_s=obra_social
    t=trabaja
    j=es_jubilado
    h=tiene_hijos
    return f"{ayn}{d}{d_n_i}{e_p}{e_s}{e_u}{v_p}{o_s}{t}{j}{h}"# devuelve todos los campos concatenados

#subprograma que se encarga de guardar los datos del archivo csv en una lista
def guardar_datos_en_lista(nombre_archivo):
    lista = []
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            lista.append(fila)
    return lista

#subprograma que se encaraga de recuperar los datos y mostrarlos
#def recuperar_datosLF():
    #print("---------Datos del archivo de longitud fija------------")
    #with open("personasLF.dat", "r", encoding="utf-8") as f:
    #    for linea in f:
    #        print(f"Apellido y Nombre: {linea[0:19]}, Direccion: {linea[20:49]}, DNI: {linea[50:57]}, Estudios Primarios: {linea[58]}, Estudios Secundarios: {linea[59]}, Estudios Universitarios: {linea[60]}, Vivienda propia: {linea[61]}, Obra social: {linea[62]}, Trabaja: {linea[63]}, Jubilado: {linea[64]}, Hijos: {linea[65]} ")

#subprograma que se encarga de mostrar el tamaño de los datos en bytes, utilizando funciones de la libreria os
def tamaño_del_archivo(nombre_archivo):
    print(f"El archivo {nombre_archivo} ocupa {os.path.getsize(nombre_archivo)} bytes")

#subprograma que reliza el inciso a)
def archivo_de_longitud_fija():
    DatosLF=[]
    lista=guardar_datos_en_lista("Personas.csv")
    for fila in lista:
        DatosLF.append(formatear_registro(fila['apellido_nombre'],fila['direccion'],fila['dni'],fila['estudios_primarios'],fila['estudios_secundarios'],fila['estudios_universitarios'],fila['vivienda_propia'],fila['obra_social'],fila['trabaja'],fila['es_jubilado'],fila['tiene_hijos']))
    with open("personasLF.dat", "w", encoding="utf-8") as f: #funcion que crea el archivo personasLF.dat
        for r in DatosLF:
            f.write(r + "\n")
    #recuperar_datosLF()
    tamaño_del_archivo("personasLF.dat")


if __name__ == "__main__":
    archivo_de_longitud_fija()
