# Estructuras Iterativas/Repetitivas
# Ciclo Exactos: yo se la cantidad exacta de repeticiones (while/for).
# Ciclo Condicionales: no se la cantidad de repeticiones (while).

# Ciclo Exactos: yo se la cantidad exacta de repeticiones (while).
'''
Realizar un programa que imprima en pantalla los números del 1 al 100.
'''
'''
i= 1 # Inicialización del contador
N= int(input("Ingrese valor máximo del contador: "))
while i<=N: # Planteo una condición (que en algún momento tiene que finalizar)
    print(i) # El orden es importante
    i= i+1 # * # Importante: evitar ciclos infinitos
'''

# Ciclo Condicionales: no se la cantidad de repeticiones (while).
'''
Realizar un programa que calcule la sumatoria de números enteros ingresados
por teclado. Finaliza el programa ingresando 0.

'''
'''
suma= 0 # Inicializo mi acumulador (sumatoria)
num= int(input("Ingrese un número: "))
while num!=0:
    # suma= suma+num
    suma+= num
    num= int(input("Ingrese un número: "))
print("La sumatoria de los números ingresados es:", suma)
'''

# Forzar la salida de un ciclo (uso de break). Esto no se recomienda, se considera una MALA práctica
'''
cont= 0
while True: # Ctrl+D: para detener
    cont += 1
    print(cont)
    if cont==100:
        break
print("Fin del programa!")
'''

# Ciclo Exactos: yo se la cantidad exacta de repeticiones (for).
'''
Realizar un programa que imprima en pantalla los números del 1 al 100.
'''
N= int(input("Ingrese el valor máximo del contador: "))
'''
for cont in range(1,N+1,1): # (inicio, fin, incremento/salto)
    print(cont)

for cont in range(1,N+1): # (inicio, fin)
    print(cont)
'''

for cont in range(N): # (fin)
    print(cont+1)

# TO-DO: operador in y el not in (lo vemos con listas)
# TO-DO: uso del break/continue (lo vemos con excepciones)
