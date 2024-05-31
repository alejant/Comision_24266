print("============================= Aulas ============================")
dia = int(input("Ingrese el número del día: 1 (lunes) a 6 (sábado): "))
if dia % 2 == 0:
    aula = "A-300"
else:
    aula = "A-315"

print("Aula:", aula)
print()
print("================= Descuentos y estacionamiento =================")
cuota = 10000
turno = input("Ingrese el turno: Mañana, Tarde o Noche: ")
materias = int(input("Ingrese la cantidad de materias: "))
if turno == "Tarde" and materias > 3:
    cuota = cuota - (cuota * 0.25)
else:
    cuota = cuota - (cuota * 0.05)
print(f'El valor de la cuota es: {cuota}')

vehiculo = input("Ingrese el vehículo en el que ingresa: Auto, Moto o Bicicleta: ")
costo_estacionamiento = 0
if vehiculo == "Auto" or vehiculo == "Moto":
    costo_estacionamiento = 300
else:
    costo_estacionamiento = 50
print(f'El costo de estacionamiento para {vehiculo} es: {costo_estacionamiento}')