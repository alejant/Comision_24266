class Cliente:
    banco= "Santa" # Atributo de clase

    # Constructor
    def __init__(self, nom):
        self.nombre= nom # Atributo de instancia
        self.saldo= 0
    
    # Mostrar info del objeto
    def __str__(self):
        cadena= "Nombre: " + self.nombre + " Saldo: " + str(self.saldo)
        return cadena
    
    def depositar(self, importe):
        self.saldo += importe

    def extraer(self, importe):
        self.saldo -= importe
    
    # getter
    def obtener_saldo(self):
        return self.saldo

# Bloque Ppal
cli1= Cliente("Ramiro")
print(cli1) # <__main__.Cliente object at 0x000001480DFC6FD0>
print("Cliente 1: " + str(cli1))
cli1.depositar(float(input("Ingrese importe a depositar: ")))
print(cli1.obtener_saldo())
print("Cliente 1: " + str(cli1))

cli2= Cliente("Sofía")
print(cli2)
cli2.saldo= 2000 # Puede acceder directamente al dato
print(cli2.saldo)

# cli1 y cli2 son dos objetos distintos con identidades distintas
print(cli1.banco)
print(cli2.banco)
