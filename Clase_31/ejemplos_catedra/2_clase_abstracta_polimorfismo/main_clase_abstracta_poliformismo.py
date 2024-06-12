from gato import Gato
from perro import Perro
from animal import Animal

# Bloque Ppal
def __main__():
    # a1= Animal() # TypeError: Can't instantiate abstract class Animal
    g1= Gato()
    # g1.mover()
    # g1.emitir_sonido()
    p1= Perro()
    animales= []
    animales.append(g1)
    animales.append(p1)

    # Muestro todos los animales de mi lista
    for animal in animales:
        animal.emitir_sonido() # Ejemplo de Poliformismo

if __name__ == "__main__":
    __main__()

print(__name__)