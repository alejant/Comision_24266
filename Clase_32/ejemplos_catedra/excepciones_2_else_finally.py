# Capturar y manejar Excepciones: voy de lo más específico a lo más genérico.
# Ejemplo de aplicación de "except, else y finally": contabilizar registros OK reg ERR y total de registros de un archivo
# Podría tener un bloque try dentro de un finally, except, etc.
try:
    num1= int(input("Ingrese un número: ")) # ValueError
    num2= int(input("Ingrese otro número: "))
    resultado= num1/num2 # ZeroDivisionError: division by zero
except ValueError:
    print("Debe ingresar un valor numérico.")
except ZeroDivisionError:
    print("El divisor no puede ser 0 (cero).")
except:
    print("Ha ocurrido un error!")
else: # Si no ocurre error alguno,...
    print("El resultado de la división es:", resultado) 
finally: # Se ejecuta SIEMPRE
    print("Fin de mi código")
    
print("Fin!")
