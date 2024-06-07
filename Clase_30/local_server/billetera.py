class Billetera:
    cantidad_billeteras = 0

    def __init__(self):
        self.__dinero = -10
        Billetera.cantidad_billeteras = Billetera.cantidad_billeteras + 1

    # @property
    # def plata(self):
    #     resultado = 100
    #     if self.__dinero > 100:
    #         resultado = self.__dinero
    #     return resultado
    @property
    def plata(self):
        return self.__calcular_plata()

    @plata.setter
    def plata(self, numero_entrada):
        if numero_entrada < 1000:
            print("No seas rata")
        self.__dinero = numero_entrada

    def __calcular_plata(self):
        resultado = 0
        if self.__dinero > 0:
            resultado = self.__dinero
        return resultado
    
    @classmethod
    def decime_algo(cls):
        print(f"Hay {cls.cantidad_billeteras} billeteras")


mi_billetera = Billetera()
otra_billetera = Billetera()
una_mas_billetera = Billetera()
# print(f"Mi dinero es {mi_billetera.__dinero}")
print(f"Mi dinero es {mi_billetera.plata}")
mi_billetera.plata = 100
print(f"Mi dinero es {mi_billetera.plata}")

Billetera.decime_algo()

    