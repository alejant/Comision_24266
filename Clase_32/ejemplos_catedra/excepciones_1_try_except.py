# Capturar y manejar Excepciones: voy de lo más específico a lo más genérico.
try:
    num1= int(input("Ingrese un número: ")) # ValueError
    num2= int(input("Ingrese otro número: "))
    resultado= num1/num2 # ZeroDivisionError: division by zero
    print(resultado) # NameError
except ValueError:
    print("Debe ingresar un valor numérico.")
except ZeroDivisionError:
    print("El divisor no puede ser 0 (cero).")
except:
    print("Ha ocurrido un error!")

print("Fin!")
