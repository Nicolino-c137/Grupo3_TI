#Se usa NumPy para el manejo de vectores/matrices y math para logaritmos en base 2.
import numpy as np
import math

#Subprograma que calcula la entropia condicional
def Entropia_condicional(Canal, px):
    H_yx = 0
    for i in range(Canal.shape[0]):          # Recorre cada fila (entrada X del canal)
        for j in range(Canal.shape[1]):      # Recorre cada columna (salida Y del canal)
            if Canal[i, j] > 0:              # Evita log(0)
                H_yx += px[i] * (-Canal[i, j] * math.log2(Canal[i, j]))
    return H_yx

#Subprograma que calcula la entropia de salida
def Entropia_salida(px, Canal):
    qy = px @ Canal  # distribución de Y: p(y) = sum_x p(x)P(y|x)
    return -np.sum([q * math.log2(q) for q in qy if q > 0])

#Subprograma que calcula la capacidad de un canal UNIFORME
def Capacidad_CUniforme(Canal,R):
    px = np.ones(R)/R                           # Distribución uniforme de entrada
    H_y = Entropia_salida(px,Canal)             # Entropía de salida
    H_yx = Entropia_condicional(Canal,px)       # Entropía condicional
    C = H_y-H_yx                                # Capacidad = I(X;Y) = H(Y) - H(Y|X)
    print(f"La capacidad de un canal {R}x{R} es: {C} bits")

#Subprograma que verifica si un canal es uniforme 
def Verificar_Uniformidad(Canal,R):
    ref = np.sort(Canal[0])                    # Ordena la primera fila
    for i in range(1, R):                      # Compara con todas las demás filas
        if not np.allclose(np.sort(Canal[i]), ref, atol=1e-8):
            return False
    return True

#Subprograma que calcula la informacion mutua
def mutual_information(px, P):
    qy = px @ P                              # Distribución de salida p(y)
    I = 0.0
    for i in range(len(px)):                 # Recorre todas las entradas
        for j in range(P.shape[1]):          # Recorre todas las salidas
            if px[i] > 0 and P[i,j] > 0 and qy[j] > 0:
                I += px[i] * P[i,j] * math.log2(P[i,j] / qy[j])
    return I


#Subprograma que usa el algoritmo blahut arimoto para calcular la capacidad de un canal NO UNIFORME y la distribucion de entrada optima que la maximiza(se uso Chatgpt) 
def blahut_arimoto(P, tol=1e-10, max_iter=1000):
    m, _ = P.shape
    px = np.ones(m) / m                       # Distribución inicial uniforme
    for _ in range(max_iter):
        qy = px @ P                           # Distribución de salida
        D = np.zeros(m)
        for i in range(m):
            for j in range(P.shape[1]):
                if P[i,j] > 0 and qy[j] > 0:
                    D[i] += P[i,j] * math.log2(P[i,j] / qy[j])
        new_px = px * (2 ** D)                 # Actualización Blahut-Arimoto
        new_px /= new_px.sum()                 # Normaliza para que sume 1
        if np.max(np.abs(new_px - px)) < tol:  # Criterio de convergencia
            px = new_px
            break
        px = new_px
    return mutual_information(px, P), px

#Subprograma que muestra la capacidad del canal no uniforme y el p(xi) optimo
def Capacidad_NOUniforme(Canal,R):
    C, px_opt = blahut_arimoto(Canal)
    print(f"La capacidad de un canal {R}x{R} es: {C} bits")
    print("p(x) óptimo:", px_opt)


#Subprograma que decide que capacidad del canal se va calcular de acuerdo al tipo(UNIFORME o NO UNIFORME)
def Capacidad_Canal(Canal,R):
    if Verificar_Uniformidad(Canal,R)==True:
        Capacidad_CUniforme(Canal,R)
    else:
        Capacidad_NOUniforme(Canal,R)


if __name__=="__main__":
    print("2_ Canal de orden 2")
    print("3_ Canal de orden 3")
    print("4_ Canal de orden 4")
    R = int(input("Por favor, ingrese un valor para el canal cargado: "))
    canal = np.array([
        [0.6, 0.3, 0.1],
        [0.2, 0.5, 0.3],
        [0.4, 0.2, 0.4]
    ])
    Capacidad_Canal(canal,R)


    