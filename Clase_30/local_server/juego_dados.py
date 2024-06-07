import random

class Dado:
    def __init__(self):
        self.__valor = 1

    def tirar(self):
        self.__valor = random.randint(1, 6)

    def imprimir(self):
        print(f"Salio el {self.__valor}")

    @property
    def valor(self):
        return self.__valor


    # def hacer_trampa(self, nuevo_valor):
    #     self.__valor = nuevo_valor


class Juego():
    def __init__(self) -> None:
        self.__dado_1 = Dado()
        self.__dado_2 = Dado()

    
    def jugar(self):
        print("tirando dados")
        self.__dado_1.tirar()
        self.__dado_2.tirar()
        resultado = self.__dado_1.valor == self.__dado_2.valor

        while (not resultado):
            print("No ganaste tirando de nuevo")
            self.__dado_1.tirar()
            self.__dado_2.tirar()
            resultado = self.__dado_1.valor == self.__dado_2.valor
        print("Ganaste")


mi_super_juego = Juego()
mi_super_juego.jugar()




        

        