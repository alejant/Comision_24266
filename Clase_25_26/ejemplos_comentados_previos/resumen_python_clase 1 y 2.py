'''
5) Escribe un programa que pida dos números y escriba en 
la pantalla cual es el mayor.

'''
'''
num1= int(input("Ingrese un número: "))
num2= int(input("Ingrese otro número: "))

# Condicionales (doble)
if num1!=num2:
    if num1>num2:
        print("El valor mayor es", num1)
    else:
        print("El valor mayor es", num2)
else:
    print("Los números son IGUALES!")
'''

'''
6) Escribe un programa que pida 3 números y escriba en la pantalla 
el mayor de los tres.
3 pasos para programar:
1) Objetivo (Qué) -> pre y pos-condiciones (entradas y salidas)
2) Estrategia (Algoritmo) (Cómo) -> pasos
3) Programar -> Lenguaje (Java, PHP, Python, etc.)

'''
# 1) Ingresar los valores de entrada
# num1= int(input("Ingrese un número: "))
# num2= int(input("Ingrese un número: "))
# num3= int(input("Ingrese un número: "))

'''
# Me devuelve el mayor ESTRICTO
if num1>num2 and num1>num3:
    print("Mayor:", num1)
else:
    if num2>num1 and num2>num3:
        print("Mayor:", num2)
    else:
        if num3>num1 and num3>num2:
            print("Mayor:", num3)

# elif (else-if)
if num1>num2 and num1>num3:
    print("Mayor:", num1)
elif num2>num1 and num2>num3:
    print("Mayor:", num2)
elif num3>num1 and num3>num2:
    print("Mayor:", num3)

'''
# mayor= num1
# if num2>mayor:
#     mayor= num2
# if num3>mayor:
#     mayor= num3
# print('El valor mayor es:', mayor)

# Estructura iterativas
# while (ciclos condicionales y exactos)
'''
Ingresar valores hasta que el usuario ingrese el valor 0. 
Al final, voy a informar la sumatoria de los valores ingresados.

'''
'''
# Ejemplo ciclo condicional
suma= 0
# 1) Inicialiazar las var de mi condición
num= int(input("Ingrese un número: "))
while num!=0: # recordar INDENTACIÓN # 2) La condición
    # 3) El orden de las instrucciones dentro de mi while
    # suma= suma+num
    suma+=num
    num= int(input("Ingrese un número: ")) # 4) La instrucción que modifica mi condición
print('La sumatoria es:', suma) # El informe final
'''

'''
Crear un contador cuyo valor máximo se ingresa por teclado.
'''

# ciclo exacto
cont= 0
num= int(input("Ingrese un valor: "))
while cont<num:
    cont+=1
    print(cont)

# for
for cont in range(10): # 0 1 2 ... 9
    print(cont+1)

for cont in range(1,11): # 1 2 3 ... 10
    print(cont)

for cont in range(1,11,2): # 1 3 5 ... 9
    print(cont)

# for (for-each) # con listas
lista= [1,10,100,20,-3,40,-200]
      # 0 1  2   3  4  5  6
print(lista)
for valor in lista:
    print(valor, end=" ")
print() # Salto de línea
