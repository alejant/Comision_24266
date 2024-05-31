nombre_completo = input("Ingrese su nombre: ") # string
edad = int(input("Ingrese su edad: ")) # int
titulo = True # bool
fec_nac = input("Ingrese fecha de nacimiento: ")
matricula = float(input("Ingrese monto de la matrícula: ")) # float
cuota = matricula + 1000
arancel_especial_mensual = 12000/4
descuento = arancel_especial_mensual*0.15
arancel_especial_mensual_desc = arancel_especial_mensual - descuento

# Mostramos los datos
print()
print("=======================================================")
print("======== Universidad de Python - Inscripciones ========")
print("=======================================================")
print()
print("DATOS DE INGRESO:")
print("Nombre completo:", nombre_completo)
print("Fecha de nacimiento y edad:", fec_nac, end='')
print(" (" + str(edad) + ")")
print("Posee título?:", titulo)
print("Matrícula: " + str(matricula))
print("Cuota mensual: " + str(cuota))
print("Arancel mensual materia 'Python I':", arancel_especial_mensual)
print("Arancel mensual materia 'Python I' con descuento:", arancel_especial_mensual_desc)
