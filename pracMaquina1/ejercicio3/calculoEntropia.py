import math, os

#Leemos el archivo y lo guardamos como una secuencia de bytes
def getFuente(ruta):
    with open(ruta, "rb") as f:
        fuente = f.read()
    return fuente

#Calculamos las frecuencias de los símbolos de la fuente
def getFrecuencias(fuente):
    frecuencias = {}
    for simbolo in fuente:
        if simbolo in frecuencias:
            frecuencias[simbolo] += 1
        else:
            frecuencias[simbolo] = 1
    return frecuencias

#Calculamos las frecuencias de los bigramas de la fuente
def getFrecuenciasBigrama(fuente):
    frecuencias = {}
    for i in range(len(fuente)-1):
        bigrama = (fuente[i], fuente[i+1])
        if bigrama in frecuencias:
            frecuencias[bigrama] += 1
        else:
            frecuencias[bigrama] = 1
    return frecuencias

#Calculamos las probabilidades de los símbolos de la fuente
def probabilidadesIndependientes(frecuencias):
    p = {}
    total = sum(frecuencias.values())
    for s in frecuencias:
        p[s] = frecuencias.get(s)/total
    return p 

#Calculamos las probabilidades dependientes, es decir, P(A|B) = P(A,B)/P(B)
def probabilidadesDependientes(frecuenciasS, frecuenciasB):
    p = {}
    totalFB = sum(frecuenciasB.values())
    totalFS = sum(frecuenciasS.values())
    for (a, b), f in frecuenciasB.items():
        pAB = f/totalFB #P(A,B)
        pB = frecuenciasS.get(b, 0)/totalFS
        p[(a, b)] = pAB/pB
    return p

#Calculamos la entropía de la fuente con símbolos vistos de forma independiente
def entropia(probabilidades):
    h = 0
    for p in probabilidades.values():
        h -= p*math.log2(p)
    return h

#Calculamos la entropía de la fuente con símbolos vistos de forma dependiente
def entropiaCondicional(probabilidadesDep, probabilidadesInd):
    h = 0
    for s, p in probabilidadesInd.items():
        for (a,b), pDep in probabilidadesDep.items():
            if b == s:
                h -= p*pDep*math.log2(pDep)
    return h 

#Calculamos la redundancia relativa de la fuente
def redundancia(entropia, entropiaCond, frecuencias):
    entropiaMax = math.log2(len(frecuencias))
    print(entropiaMax)
    redundanciaInd = 1-entropia/entropiaMax
    redundanciaDep = 1-entropiaCond/entropiaMax
    print("Redundancia relativa de la fuente con símbolos vistos de forma independiente: {:.2f}%".format(redundanciaInd*100))
    print("Redundancia relativa de la fuente con símbolos vistos de forma dependiente: {:.2f}%".format(redundanciaDep*100))

if __name__ == "__main__":
    print("Cargue un archivo en la carpeta e ingrese su nombre con la extensión")
    ruta = os.getcwd()
    ruta = os.path.join(ruta, str(input()))
    fuente = getFuente(ruta)
    frecuenciasSimbolos = getFrecuencias(fuente)
    frecuenciasBigrama = getFrecuenciasBigrama(fuente)
    probInd = probabilidadesIndependientes(frecuenciasSimbolos)
    probDep = probabilidadesDependientes(frecuenciasSimbolos, frecuenciasBigrama)
    entropiA = entropia(probInd)
    entropiaCond = entropiaCondicional(probDep, probInd)
    print("Entropia de la fuente con símbolos vistos de forma independiente: {:.3f} bits".format(entropiA))
    print("Entropia de la fuente con símbolos vistos de forma dependiente: {:.3f} bits".format(entropiaCond))
    redundancia(entropiA, entropiaCond, frecuenciasSimbolos)