'''
Bloque de comentarios:
Primera clase de Python

'''
# Comentario en línea
# print
apellido="Escalante Leiva"
print("Hola Mundo")
print("Apellido:", apellido)
print("Apellido:" + apellido)

# print (sin salto)
print("Imprimir sin salto", end= "")
print("Hola Mundo")

# clear en la consola para limpiar

# ingreso de datos: input
variable= input("Ingrese un dato: ") # retorna un String
print(variable)

# Tipos de datos
varStr= "Ramiro"
varNum= -123
varFloat= 12.3 # Decimal
varBoo1= True
varBoo0= False

# conversión de tipos de datos
# str -> int
varNum2= int(input("Ingrese un número: "))
# str -> float
# varFloat2= float("Texto") # Error
varFloat3= float("12") # Error
varFloat4= float("-12.3") # Error
# int -> str
print(str(12))
varStr2= str(-12.3)

# float -> int
varFloat5= int(12.3)

print(varFloat3)
print(varFloat4)
print(varFloat5)

# reutilización de variables
# operador de asignación
# no se definen variables
# no se determina un tipo de dato para la variable
nombre= "Ramiro"
nombre= "Juan"
nombre= 12.3
nombre= True

print(nombre)

# indentación (to-do)
if True:
    print("Bloque de Verdad")
