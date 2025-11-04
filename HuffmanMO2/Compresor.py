from collections import defaultdict, Counter
from ClaseNodo import Nodo
import heapq #Para mejor eficiencia en la construcción del árbol (recomendado por Copilot)
import json

def construirArbolHuffman(frecuencias):
    heap = [Nodo(s, f) for s, f in frecuencias.items()]
    heapq.heapify(heap)
    if len(heap) == 1: #Cuando solo hay un símbolo, creamos un nodo padre con único hijo izquierdo
        unico = heapq.heappop(heap)
        return Nodo(None, unico.freq, unico, None) 
    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        nuevo = Nodo(None, n1.freq + n2.freq, n1, n2)
        heapq.heappush(heap, nuevo)
    return heap[0]

def getCodigos(nodo, prefijo="", codigos=None):
    if codigos is None:
        codigos = {}
    if nodo.simbolo is not None:
        codigos[nodo.simbolo] = prefijo or "0"
    else:
        if nodo.izq:
            getCodigos(nodo.izq, prefijo + "0", codigos)
        if nodo.der:
            getCodigos(nodo.der, prefijo + "1", codigos)
    return codigos

#Generamos códigos pseudo ASCII para los contextos para los primeros 2 símbolos iniciales
def getPseudoAscii(contextos):
    n = len(contextos)
    bits = len(bin(n - 1)) - 2  # cantidad mínima de bits necesarios
    codigos = {}
    for i, contexto in enumerate(contextos):
        codigos[contexto] = format(i, f'0{bits}b')
    return codigos

#Como es de orden 2 consideramos pares de símbolos como contexto
def huffmanMarkovOrden2(texto):
    transiciones = defaultdict(Counter) #Diccionario de contadores para cada contexto
    for i in range(len(texto) - 2):
        contexto = texto[i:i + 2]
        simbolo = texto[i + 2]
        transiciones[contexto][simbolo] += 1
    #Como la cadena se repite sistemáticamente, añadimos la transición de los últimos 2 símbolos al inicio
    transiciones[texto[-2:]][texto[0]] += 1
    arboles = {}
    for contexto, frecuencias in transiciones.items():
        arbol = construirArbolHuffman(frecuencias)
        codigos = getCodigos(arbol)
        arboles[contexto] = codigos
    codigosAscii = getPseudoAscii(list(arboles.keys()))
    return arboles, codigosAscii

#A partir de los 2 primeros caracteres (en pseudo ASCII) y los códigos de Huffman generados, comprimimos el texto
#El consecuente carácter se codifica según el contexto de los 2 caracteres previos, luego se avanza 1 carácter y se repite el proceso
def comprimir(texto, arboles, codigosAscii):
    contexto_inicial = texto[:2]
    comprimido = codigosAscii.get(contexto_inicial)
    for i in range(2, len(texto)):
        contexto = texto[i - 2:i]
        simbolo = texto[i]
        if contexto in arboles and simbolo in arboles[contexto]:
            comprimido += arboles[contexto][simbolo]
        else:
            comprimido += f"[{simbolo}]"
    return comprimido


def compresor(texto, archivo_salida="HuffmanMO2/comprimido.txt"): 
    arboles, codigosAscii = huffmanMarkovOrden2(texto)
    comprimido = comprimir(texto, arboles, codigosAscii)
    print("Texto original:", texto)
    print("Texto comprimido:", comprimido)
    datos = {
        "codigosAscii": codigosAscii,
        "arboles": arboles,
        "comprimido": comprimido
    }
    with open(archivo_salida, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)