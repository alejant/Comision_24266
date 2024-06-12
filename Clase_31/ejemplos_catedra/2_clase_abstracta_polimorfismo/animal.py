from abc import ABC, abstractmethod

class Animal(ABC):
    # Si comento el decorador, error al instanciar
    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def emitir_sonido(self):
        print("Animal emite sonido: ", end="")
