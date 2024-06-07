from class_cuenta import Cuenta
from class_banco import Banco

# Prog Ppal
# Creo un objeto de tipo Cuenta
cuenta1= Cuenta("Ramiro")
cuenta1.depositar(1000)
if not cuenta1.extraer(1100):
    print("Ha ocurrido un error. No se realizó la extracción.")
# print(cuenta1)
# Creación de otra instancia (otro objeto Cuenta)
cuenta2= Cuenta("Laura")
# print(cuenta2)

# Creo un objeto de tipo Banco que contendrá cuentas (lista clientes)
banco1= Banco("Santa")
print(banco1)
banco1.agregar_cliente(cuenta1)
banco1.agregar_cliente(cuenta2)
print(banco1)

# No puedo acceder al atributo privado
# print(cuenta1.__saldo) # AttributeError: 'Cuenta' object has no attribute '__saldo'
print(cuenta1.saldo) # Obteniendo el saldo mediante su getter
# cuenta1.saldo= 1000 # AttributeError: can't set attribute

# Accedo al atributo de clase "banco", teniendo la Clase Banco pierde sentido este atributo en Cuenta
# print(cuenta1.banco)
# print(cuenta2.banco)

# Para pensar encapsulamiento
# cuenta1.saldo= cuenta1.saldo+10
# cuenta1.saldo= -200 # AttributeError: can't set attribute
cuenta1.titular= "Pablo" # Cuenta tiene un setter para titular
print(cuenta1)
