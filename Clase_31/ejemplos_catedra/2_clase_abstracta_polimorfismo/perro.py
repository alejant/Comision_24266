from animal import Animal

class Perro(Animal):

#    Si no implemento el método mover -> ERROR
    def mover(self):
        print("El perro se mueve.")

    def emitir_sonido(self):
        super().emitir_sonido()
        # pass
        print("Guau!")

# Prog ppal
if __name__ == '__main__':
    print("valor de __name__ para la clase perro:", __name__)