# Ejemplo: quiero LANZAR (no capturar) una excepción si el número ingresado es NEGATIVO. 
# Posible uso del raise: def ingresar_entero_positivo
class NumeroNegativoError(Exception):
    pass # Ejemplo para crear una Excepción propia

num= int(input("Ingrese un número: "))
if num<0:
    # raise Exception("El número no puede ser negativo.") # Invoco el método especial: __init__ (constructor)
    raise NumeroNegativoError("El número no puede ser negativo.") # Invoco el método especial: __init__ (constructor)
print(num)
