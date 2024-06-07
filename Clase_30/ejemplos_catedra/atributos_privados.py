class Cliente:
    ''' 
    Ocultamiento de información:
    
    Los métodos y atributos débilmente privados tienen un único guion bajo al principio. 
    Esto señala que son privados, y no deberían ser utilizados por código externo. 
    Sin embargo, es en su mayor parte solo una convención, y no impide que el código externo los acceda.
    Su único efecto verdadero es que from module_name import * no importará a las variables que empiecen 
    con un único guion bajo.

    Los métodos y atributos fuertemente privados tienen doble guion bajo al principio de sus nombres. 
    Esto hace que sus nombres sean decorados, lo cual significa que no pueden ser accedidos desde afuera 
    de la clase.
    El propósito de esto no es asegurar que se mantengan privados, sino de evitar errores en caso de 
    que existan subclases que tengan métodos o atributos con los mismos nombres.
    
    '''
    _direccion_banco= "Calle 123" # Atributo debilmente privado
    __banco= "Santa" # Atributo fuertemente privado

    # Constructor
    def __init__(self, nombre):
        self.__nombre= nombre # Atributo de instancia
        self.__saldo= 0
    
    # Mostrar info del objeto
    def __str__(self):
        cadena= "Nombre: " + self.nombre + " Saldo: " + str(self.saldo)
        return cadena
    
    # getter para saldo
    @property
    def saldo(self):
        return self.__saldo

    # El orden es importante: 1ro el getter y luego el setter
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre= nombre

    def depositar(self, importe):
        self.saldo += importe

    def extraer(self, importe):
        self.saldo -= importe
    
    # el método obtener saldo hace uso del getter del atributo saldo
    def obtener_saldo(self):
        return self.saldo

# Bloque Ppal
cli1= Cliente("Ramiro")
# print(cli1.__saldo) # AttributeError: 'Cliente' object has no attribute '__banco'
print(cli1.saldo) # Obtengo el saldo pero a través del getter
print(cli1.nombre)
cli1.nombre = "Ezequiel Ramiro" # Establezco el nombre pero a través del setter
                                # La forma de llamar al setter es asignándole un valor
print(cli1)

# Nota: Los métodos con nombres decorados pueden aún ser accedidos externamente pero por un nombre diferente.
#       El atributo __nombre de la clase Cliente puede ser accedido externamente con _Banco__nombre.
# print(cli1.__banco) # AttributeError
print(cli1._Cliente__banco)
