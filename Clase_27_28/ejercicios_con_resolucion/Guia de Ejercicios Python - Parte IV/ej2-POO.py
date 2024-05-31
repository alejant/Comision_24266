'''
2. Implementar una nueva clase llamada Estudiante. Esta clase tendrá como atributos 
su nombre y su nota. Definir los métodos para inicializar sus atributos,
imprimirlos y mostrar un mensaje que indique: “Promocionó” (nota >= 7),
“Rinde final” (nota >= 4) o “Desaprobó”.
Definir tres objetos de la clase Alumno, cada uno con una condición
de aprobación distinta.
 
'''

class Estudiante: 

    def inicializar(self, nombreCompleto, nota): # Método constructor
        self.nombreCompleto = nombreCompleto # Atributo de instancia
        self.nota = nota # Atributo de instancia
    
    def imprimir(self): # Método para mostrar datos
        print(f'Nombre completo: {self.nombreCompleto.title()} - Nota: {self.nota}')
        if self.nota >= 7:
            print("Promocionó")
        elif self.nota >= 4:
            print("Rinde final")
        else:
            print("Desaprobó")
        print()

# Programa principal

alumno1 = Estudiante() # Creamos el objeto
alumno1.inicializar("Juan Serrano", 8)
alumno1.imprimir()

alumno2 = Estudiante() # Creamos el objeto
alumno2.inicializar("Luisa López", 4)
alumno2.imprimir()

alumno3 = Estudiante() # Creamos el objeto
alumno3.inicializar("Diego Fernández", 2)
alumno3.imprimir()