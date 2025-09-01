#Para poder realizar la validación de un CUIT/CUIL se debe de seguir un algoritmo matemático conocido como algoritmo módulo 11
#el cual se encuentra bien explicado en el siguiente link https://todocalculadoras.com.ar/calcular-dni-argentino/

#El CUIT/CUIL consta de 11 dígitos, los primeros 10 dígitos son el número base y el último dígito es el dígito verificador.
def validar(cuit):
    retorno = False
    if len(cuit) == 11:
        #El algoritmo módulo 11 utiliza una serie de pesos para cada posición del número base.
        base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        sumatoria = 0
        for i in range(10):
            sumatoria += int(cuit[i])*base[i]
        resto = sumatoria%11
        #Existen 3 reglas para determinar el dígito verificador, si el resto es 0, si el resto es 1 y si el resto es mayor a 1.
        if resto == 0:
            retorno = 0 == int(cuit[10])
        elif resto == 1:
            cuit[0] = "2"
            cuit[1] = "3"
            retorno = validar(cuit)           
        else:
            retorno = (11-resto) == int(cuit[10])
    return retorno

if __name__ == "__main__":
    cuit = input("Ingrese un CUIT/CUIL sin guiones ni espacios: ")
    if validar(cuit):
        print("CUIT/CUIL válido")
    else:
        print("CUIT/CUIL inválido")