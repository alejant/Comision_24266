'''
1. Implementar una clase llamada Estudiante que tendrá como atributos (variables)
su nombre, su apellido, dni y dos métodos (funciones), uno de dichos métodos
inicializará los atributos y el siguiente método los mostrará en pantalla.
Definir dos objetos de la clase Estudiante e incorporar una variable de clase (piernas).

'''

class Estudiante: # Creamos la clase (sustantivo 1° letra mayúscula)

    piernas = 2 # Atributo / variable de clase

    def inicializar(self, nombre, apellido, dni): # Método constructor
        self.nombre = nombre # Atributo de instancia
        self.apellido = apellido # Atributo de instancia
        self.dni = dni # Atributo de instancia
    
    def imprimir(self): # Método para mostrar datos
        print(f'Apellido y nombre: {self.apellido.upper()}, {self.nombre}\nDNI: {self.dni}')

# Programa principal
estud1 = Estudiante() # Creamos un objeto basado en la clase Estudiante
estud1.inicializar("Juan Pablo", "Nardone", 12345678) # Llamamos al constructor con un nombre
estud1.imprimir() # Mostramos los datos

estud2 = Estudiante() 
estud2.inicializar("Luciana", "Pérez", 31234567)
estud2.imprimir() 

print(f'Los estudiantes tienen {Estudiante.piernas} piernas')
print(f'{estud1.nombre} tiene {estud1.piernas} piernas')
print(f'{estud2.nombre} tiene {estud2.piernas} piernas')

print()
estud1.piernas = 4
print(f'{estud1.nombre} tiene {estud1.piernas} piernas') # 4 piernas
estud2.nombre = "Fernanda"
print(f'{estud2.nombre} tiene {estud2.piernas} piernas') # 2 piernas

estud1.edad = 37 # Podemos agregar un atributo de instancia
print(estud1.edad)
print(estud2.edad) # Error, no tiene ese atributo