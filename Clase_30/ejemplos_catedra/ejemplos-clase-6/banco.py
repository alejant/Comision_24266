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

class Banco:
    def __init__(self):
        self.cli1= Cliente("Juan")
        self.cli2= Cliente("Ana")
        self.cli3= Cliente("Pedro")
        clientes= [] # TO-DO
        
    def simular_depositos(self):
        self.cli1.depositar(100)
        self.cli2.depositar(100)
        self.cli3.depositar(200)

    def simular_extracciones(self):
        self.cli1.extraer(150)

    def __str__(self):
        cadena= str(self.cli1) + "\n"+ str(self.cli2) + "\n"+ str(self.cli3)
        return cadena

# Bloque Ppal
banco1= Banco()
print(banco1)
