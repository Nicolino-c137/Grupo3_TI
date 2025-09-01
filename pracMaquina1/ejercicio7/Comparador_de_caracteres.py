#Este codigo utiliza un algoritmo llamado Jaro Winkler util para la comparacion de cadenas
#Devuelve un valor entre 0 y 1 (o un porcentaje entre 0% y 100%).
#0 significa que son completamente diferentes.
#1 significa que son idénticas

# Como se obtiene este valor?

#     PASO 1
#Definir la ventana de coincidencia (ventana)
#Para cada letra en la primera cadena, se busca coincidencias en la segunda dentro de un rango (ventana).
#Esto evita que letras muy alejadas cuenten como coincidencias.
def ventana(c1,c2):
    return max(len(c1),len(c2))//2-1

#     PASO 2
#Encontrar coincidencias (coincidencias)
def coincidencias(c1,c2):
    #Busca los caracteres que coinciden entre c1 y c2 dentro de la ventana permitida.
    distancia_match=ventana(c1, c2)
    #Arreglos que marcan qué caracteres coinciden en cada cadena
    c1_matches=[False]*len(c1)
    c2_matches=[False]*len(c2)
    m=0 #cantidad de coincidencias
    for i in range(len(c1)):
        #Defino el rango donde voy a buscar coincidencias para el caracter c1[i]
        start=max(0,i-distancia_match)
        end=min(i+distancia_match+1,len(c2))
        for j in range(start, end):
            #Si hay coincidencia y todavía no se usó ese caracter en c2
            if not c2_matches[j] and c1[i]==c2[j]:
                c1_matches[i]=True
                c2_matches[j]=True
                m+=1
                break    
    return m, c1_matches, c2_matches

#     PASO 3
#Calcular transposiciones
def transposiciones(c1,c2,c1_matches,c2_matches):
    #Extraigo los caracteres que coincidieron en cada cadena
    s1_coinc=[c1[i] for i in range(len(c1)) if c1_matches[i]]
    s2_coinc=[c2[j] for j in range(len(c2)) if c2_matches[j]]
    #Cuento las posiciones donde esos caracteres coincidentes están desordenados
    t=sum(ch1!=ch2 for ch1,ch2 in zip(s1_coinc, s2_coinc))
    return t//2 #Se divide entre 2 según la fórmula de Jaro

#     PASO 4
#Calcular similitud Jaro
def jaro(l1,l2,m,t):
    #Fórmula de similitud de Jaro
    return 1/3*(m/l1+m/l2+(m-t)/m)

#     PASO 5(si y solo si se cumple que exista almenos un caracter inicial igual)
def ajuste_winkler(j,l):
    #Ajuste Winkler: favorece coincidencias en el prefijo
    return j+(l*0.1*(1-j))

def prefijo_comun_inicial(c1, c2):
    #Cuenta cuántos caracteres iniciales son iguales (máximo 4)
    i=0
    while i<min(len(c1),len(c2)) and c1[i]==c2[i] and i<4:
        i+=1
    return i

def resultado(r):
    #Imprime el resultado como porcentaje
    print("Las cadenas coinciden en un: ",r*100," %")


def jaro_winkler(c1,c2):
    #Algoritmo principal
    m, c1_matches, c2_matches=coincidencias(c1,c2)
    if m==0:
        #si no hay coincidencias
        resultado(m)
    else:
        t=transposiciones(c1,c2,c1_matches,c2_matches) #transposiciones
        j=jaro(len(c1),len(c2),m,t)                    #similitud Jaro
        l=prefijo_comun_inicial(c1,c2)                 #prefijo común inicial
        if l>0 and l<=4:
           resultado(ajuste_winkler(j,l))    #aplica el ajuste Winkler
        else:
            resultado(j) #devuelve solo Jaro
    return


if __name__=="__main__":
    c1="Juan"
    c2="Jaun"
    jaro_winkler(c1.lower(),c2.lower())
