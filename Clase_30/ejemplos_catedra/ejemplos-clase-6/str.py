class Empleado:
    # Método especial __init__ (Constructor)
    def __init__(self):
        self.nombre= input("Ingrese el nombre del empleado: ")
        self.sueldo= float(input("Ingrese su sueldo: "))
    
    # Método especial __str__
    def __str__(self):
        cadena= "Nombre: " + self.nombre + ", Sueldo: " + str(self.sueldo)
        return cadena # Devuelve un str

# Bloque Ppal
# Instanciando el objeto de tipo Empleado
emp1= Empleado()
print(emp1)

# TO-DO: Actividad Práctica Nro 3

# Más info: http://www.pdep.com.ar/material/apuntes hay muy buenos apuntes si quieren profundizar mas en los conceptos del paradigma.
