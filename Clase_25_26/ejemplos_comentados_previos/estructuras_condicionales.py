'''
Problema:
Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en
pantalla indicando que debe abonar impuestos.

'''
# Estructura condicional simple
'''
sueldo= float(input("Ingrese su sueldo: "))
if sueldo>3000:
    print("Debe abonar impuestos.")

print("Fin del programa!")
'''

# Estructura condicional doble
'''
Realizar un programa que solicite ingresar dos números distintos y muestre por pantalla el
mayor de ellos.

'''
'''
num1= int(input("Ingrese un número: "))
num2= int(input("Ingrese otro número (distinto): "))
if num1>num2: # Bloque de verdad
    print("num1 es mayor.")
else: # Bloque de falsedad
    print("num2 es mayor.")
'''

'''
# Estructuras condicionales anidadas
num1= int(input("Ingrese un número: "))
num2= int(input("Ingrese otro número (distinto): "))
if num1!=num2:
    if num1>num2: # Bloque de verdad
        print("num1 es mayor.")
    else: # Bloque de falsedad
        print("num2 es mayor.")
else:
    print("Error! Los números NO son distintos!")
'''

# if-else-elif
'''
Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el
promedio e imprima alguno de estos mensajes:
    Si el promedio es >=7 mostrar "Promocionado".
    Si el promedio es >=4 y <7 mostrar "Regular".
    Si el promedio es <4 mostrar "Reprobado".
    Agrego a la consigna: Si el promedio es entre 3 y 4 -> Recupera

'''
nota1= int(input("Ingrese nota 1: "))
nota2= int(input("Ingrese nota 2: "))
nota3= int(input("Ingrese nota 3: "))
promedio= (nota1+nota2+nota3)/3

print("El promedio es:", promedio)
'''
if promedio >= 7:
    print("Promocionado")
else:
    if promedio >= 4 and promedio < 7:
    # if 4 <= promedio < 7:
        print("Regular")
    else:
        print("Reprobado")
'''
# Estructura condicional múltiple/Alternativa Múltiple 
if promedio >= 7:
    print("Promocionado")
elif promedio >= 4 and promedio < 7:
    print("Regular")
elif promedio >= 3 and promedio < 4:
    print("Recupera")
else:
    print("Reprobado")
