import json

def bytes_a_bits(data):
    """Convierte una secuencia de bytes en un string de bits."""
    return ''.join(f'{byte:08b}' for byte in data)

def descomprimir(archivo_comprimido="comprimido.bin", archivo_cabecera="cabecera.json"):
    # --- 1. Cargar la cabecera JSON (diccionarios de Huffman y pseudo ASCII) ---
    with open(archivo_cabecera, "r", encoding="utf-8") as f:
        cabecera = json.load(f)
    arboles = cabecera["arboles"]
    codigosAscii = cabecera["codigosAscii"]

    # --- 2. Leer el archivo comprimido en binario ---
    with open(archivo_comprimido, "rb") as f:
        datos_binarios = f.read()

    # --- 3. Convertir los bytes a una cadena de bits ---
    comprimido = bytes_a_bits(datos_binarios)

    # --- 4. Reconstruir el texto ---
    ascii_a_contexto = {v: k for k, v in codigosAscii.items()}  # Invertimos para buscar el contexto inicial
    bits_contexto = len(next(iter(codigosAscii.values())))      # Cuántos bits ocupa el contexto inicial
    contexto_inicial_bin = comprimido[:bits_contexto]           # Primeros bits = contexto inicial
    contexto_actual = ascii_a_contexto[contexto_inicial_bin]
    texto = contexto_actual
    i = bits_contexto

    # --- 5. Decodificar los símbolos ---
    while i < len(comprimido):
        arbol_codigos = arboles.get(contexto_actual, None)
        if arbol_codigos is None:
            break
        buffer = ""
        while i < len(comprimido):
            buffer += comprimido[i]
            i += 1
            if buffer in arbol_codigos.values():
                simbolo = [k for k, v in arbol_codigos.items() if v == buffer][0]
                texto += simbolo
                contexto_actual = texto[-2:]
                break
    if texto.endswith(texto[:1]):
        texto = texto[:-1] 

    # --- 6. Guardar y mostrar el resultado ---
    print("Texto descomprimido:", texto)
    with open("descomprimido.txt", "w", encoding="utf-8") as f:
        f.write(texto)