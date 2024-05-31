# sintaxis básica para definir (declarar) una función en Python
def nombre_funcion():
    # intrucciones
    print("Hola Mundo!")

def imprimir_hola(N, msj): # N: es un parámatro de mi fx
    # instrucciones
    nombre_funcion() # Llamado de un fx dentro de otra fx

    for i in range(N): # i es una variable local
        print(msj)
    print("i:", i)
    print("cant:", cant) # cant es una variable GLOBAL (NO se recomienda)

# Programa Principal
# llamada a una función (invocar)
nombre_funcion()

# Validación de N
cant= int(input("Ingrese cantidad de repeticiones: "))
while cant<=0:
    print("Error, dato no válido!")
    cant= int(input("Ingrese cantidad de repeticiones: "))

imprimir_hola(cant, "Hola Ramiro!") # No necesariamente se tiene que llamar N
# imprimir_hola(10) # Esta fx tiene 1 (un) sólo argumento

# print(i) # Error: porque i es una variable local
