def descomprimir(comprimido, arboles, codigosAscii):
    # Invertimos el diccionario para buscar el contexto inicial por su código pseudo ASCII
    ascii_a_contexto = {v: k for k, v in codigosAscii.items()}
    
    # Recuperamos los primeros bits del contexto inicial
    bits_contexto = len(next(iter(codigosAscii.values())))
    contexto_inicial_bin = comprimido[:bits_contexto]
    contexto_actual = ascii_a_contexto[contexto_inicial_bin]
    texto = contexto_actual
    i = bits_contexto
    # Recorremos el texto comprimido
    while i < len(comprimido):
        arbol_codigos = arboles.get(contexto_actual, None)
        if arbol_codigos is None:
            break
        buffer = ""
        while i < len(comprimido):
            buffer += comprimido[i]
            i += 1
            if buffer in arbol_codigos.values():
                # Encontramos un símbolo
                simbolo = [k for k, v in arbol_codigos.items() if v == buffer][0]
                texto += simbolo
                contexto_actual = texto[-2:]
                break
    return texto