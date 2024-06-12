from class_Vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, color, ruedas, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.cilindrada= cilindrada

    def __str__(self):
        return super().__str__() + " Cilindrada: " + str(self.cilindrada) + "."

    def avanzar(self):
        super().avanzar()
        print("El auto avanza.")

# Prog ppal
def __main__():
    print("Soy parte del programa ppal del archivo class_Auto.py")

if __name__=='__main__':
    __main__()
