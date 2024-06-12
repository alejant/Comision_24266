'''
Herencia Simple, Módulos y método __main__

'''
class Vehiculo():
    def __init__(self, color, ruedas):
        self.color= color
        self.ruedas= ruedas
    
    def __str__(self):
        return f'Color: {self.color}, Cantidad de ruedas: {self.ruedas}.'

    def avanzar(self):
        pass # print ('Por ahora no hago nada porque soy un Vehículo "sin" comportamiento asociado.')
