#Para poder realizar la validación de un CUIT/CUIL se debe de seguir un algoritmo matemático conocido como algoritmo módulo 11
#el cual se encuentra bien explicado en el siguiente link https://todocalculadoras.com.ar/calcular-dni-argentino/

#El CUIT/CUIL consta de 11 dígitos, los primeros 10 dígitos son el número base y el último dígito es el dígito verificador.
def validar(cuit):
    retorno = False
    if len(cuit) == 11:
        #El algoritmo módulo 11 utiliza una serie de pesos para cada posición del número base.
        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        sumatoria = 0
        #Se calcula la sumatoria del producto de cada dígito por su peso correspondiente y se obtiene el resto de la división por 11
        for i in range(10):
            sumatoria += int(cuit[i])*base[i]
        resto = sumatoria%11
        #Existen 3 reglas para determinar el dígito verificador
        #Si el reto es 0, entonces el dígito verificador debe ser 0
        if resto == 0:
            retorno = 0 == int(cuit[10])
        #Si el resto es 1, entonces se debe cambiar el prefijo del CUIT/CUIL a 23 y volver a calcular
        elif resto == 1:
            cuit[0] = "2"
            cuit[1] = "3"
            retorno = validar(cuit)
        #Si el resto es cualquier otro número, entonces el dígito verificador debe ser 11 menos el resto          
        else:
            retorno = (11-resto) == int(cuit[10])
    return retorno

if __name__ == "__main__":
    cuit = input("Ingrese un CUIT/CUIL sin guiones ni espacios: ")
    if validar(cuit):
        print("CUIT/CUIL válido")
    else:
        print("CUIT/CUIL inválido")