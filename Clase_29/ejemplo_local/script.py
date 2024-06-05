class Persona():
    poblacion=0
    def __init__(self, nombre_asignado):
        Persona.poblacion = Persona.poblacion + 1
        self.nombre = nombre_asignado
        self.apellido = "JEVUS"

    def renombrar(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def __str__(self):
        # return "Se llama " + self.nombre
        return f"Se llama {self.nombre}"

    def __repr__(self):
        return f"{self.nombre} - {self.apellido}"


variable_1 = Persona("Alejandro")
variable_2 = Persona()
variable_2.renombrar("Juan")

print(variable_1)
print(variable_2)
print(variable_1 == variable_2)


