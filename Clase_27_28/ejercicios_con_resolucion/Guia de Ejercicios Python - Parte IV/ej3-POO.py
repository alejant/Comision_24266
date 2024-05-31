'''
3. Crear una clase que represente una Materia de la universidad. Definir como atributos su nombre, carrera, duración en meses y un atributo de clase booleano para definir que todas las materias no son promocionables. Desarrollar un método __init__ para incializarlos. Crear un método para imprimir los datos del objeto, luego sustituirlo por el método __str__(). Crear dos objetos. Eliminar uno de ellos a través del método __del__().

'''

class Materia: 
    promo = False #Atributo de clase
    
    # Nuevo método constructor
    def __init__(self, nombre, carrera, duracion): # Permite instanciar y agregar valores a los atributos
        self.nombre = nombre
        self.carrera = carrera
        self.duracion = duracion
        
    def imprimir(self):
        print(f'Materia: {self.nombre.title()}\nCarrera: {self.carrera.upper()}\nDuración: {self.duracion} meses\nPromocionable: {self.promo}')

    def __str__(self): # Reemplaza al método imprimir
        return f'Materia: {self.nombre.title()}\nCarrera: {self.carrera.upper()}\nDuración: {self.duracion} meses\nPromocionable: {self.promo}'

    def __del__(self): # Elimina el objeto
        print(f'{self.nombre} ha sido eliminada')

# Programa principal
materia1 = Materia("introd. a python", "ing. en informática", 4)
# materia1.imprimir()
print(materia1)
print()
materia2 = Materia("inteligencia artificial", "ing. en informática", 8)
print(materia2)
print()
# del materia2