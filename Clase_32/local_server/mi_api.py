
from paquete.adios.despedidas import despedir

class NumeroNegativoError(Exception):
    pass

def calcular_division(numero, divisor):
    try:
        mi_resultado = None
        despedir()
        print("Arranco haciendo calculos")
        # if divisor < 0:
        #     raise NumeroNegativoError("veo numeros negativos")
        # assert divisor >= 0, "Numero menor o igual a cero"
        prueba = 3 / 0
        mi_resultado = numero / divisor
        print("estoy haciendo muchos calculos")
    except NumeroNegativoError as nnE:
        pass        
    except ZeroDivisionError as zdErrror:
        print(zdErrror)
        print("no tengo ni idea, hago lo que puedo")
        mi_resultado = 0
    except TypeError as typeError:
        print(typeError)
        print("mandaste fruta")
    else: 
        print("Soy el mejor programa del munod")
    finally:
        print("ESTOY CANSADO JEFE")

    return mi_resultado


# Comienza programa 
numero = 0
otro_numero = 2

try:
    print("comienzo a hacer calculos")
    resultado = calcular_division(4, -1)
    print("sigo haciendo calculos")
    resultado = calcular_division(4, 2)
    print("sigo haciendo calculos")
    otro_resultado = calcular_division(4, "dos")
    print("sigo haciendo calculos")
    resultado = calcular_division(otro_numero, numero)

except BaseException as be:
    print(be)
    print("Algo saio mal")


print("Hice todo los calculos")




