'''
Consigna Actividad Opcional POO Banco:
Desarrollar un sistema para gestionar las altas y el listado de los Clientes de un Banco utilizando los siguintes conceptos:
Listas, Clases y Objetos, Métodos especiales, Herencia y Polimorfismo, Clases y Métodos Abstractos.
Opcional: realizar los métodos para modificar, eliminar, buscar un Cliente en el Banco.

Sistema Banco:
Cliente: clase (abstracta)
Atributos:
    titular
    saldo
Métodos:
init
str
depositar
extraer  (abstracto)
getter:
    saldo

ClienteEstandar: clase
Métodos:
depositar
extraer (sobreescribo)

ClienteGold: clase
Atributo:
    descubierto
Métodos:
depositar
extraer (sobreescribo)
str (sobreescribir)
getter:
    descubierto

Banco: clase
import:
    ClienteEstandar
    ClienteGold
init
str
atributos:
    clientes (array)
métodos:
    cargar_cliente
    listar_clientes (recorre todas las cuentas y las muestra, por línea muestra sólo una cuenta. Sirve para ver Polimorfismo)
    extraer un valor de todos los clientes.
    etc.

Agregar registro de movimientos. 

'''
