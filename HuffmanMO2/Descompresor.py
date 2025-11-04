def descomprimir(comprimido, arboles, codigosAscii):
    ascii_a_contexto = {v: k for k, v in codigosAscii.items()} # Invertimos el diccionario para buscar el contexto inicial por su código pseudo ASCII
    bits_contexto = len(next(iter(codigosAscii.values()))) # Determinamos cuántos bits ocupa el contexto inicial
    contexto_inicial_bin = comprimido[:bits_contexto] # Tomamos los primeros bits del texto comprimido para identificar el contexto inicial
    contexto_actual = ascii_a_contexto[contexto_inicial_bin] # Buscamos el contexto correspondiente
    texto = contexto_actual # Inicializamos el texto descomprimido con el contexto inicial
    i = bits_contexto # Posición actual en el texto comprimido
    # Recorremos el texto comprimido
    while i < len(comprimido):
        arbol_codigos = arboles.get(contexto_actual, None)
        if arbol_codigos is None:
            break # Si no hay árbol para este contexto, se detiene
        buffer = "" 
        # Acumulamos bits hasta encontrar un código válido en el árbol
        while i < len(comprimido):
            buffer += comprimido[i]
            i += 1
            if buffer in arbol_codigos.values():
                # Encontramos un símbolo asociado a este código
                simbolo = [k for k, v in arbol_codigos.items() if v == buffer][0]
                texto += simbolo
                # Actualizamos el contexto a los últimos dos caracteres del texto reconstruido
                contexto_actual = texto[-2:]
                break
    print("Texto descomprimido:", texto)
    with open("HuffmanMO2/descomprimido.txt", "w", encoding="utf-8") as f:
        f.write(texto)