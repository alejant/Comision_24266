from animal import Animal

class Gato(Animal):

#    Si no implemento el método mover -> ERROR
    def mover(self):
        print("El gato se mueve.")

    def emitir_sonido(self):
        super().emitir_sonido()
        print("Miau!")

