nota1 = float(input("Ingrese la nota del primer parcial: "))
nota2 = float(input("Ingrese la nota del segundo parcial: "))
promedio = (nota1 + nota2) / 2
print()
print("El promedio de las notas es:", promedio)

if nota2 >= 7:
    print("Aprobó el segundo parcial")
else:
    print("Desaprobó el segundo parcial")

if nota2 > nota1:
    estado = "Mejoró su desempeño"
else:
    if nota1 == nota2:
         estado = "Mantuvo la nota"
    else:
        estado = "Empeoró su desempeño"
print(f'Progreso del 1er al 2do parcial: {estado}')

if promedio >= 7:
    print("Promocionó la materia")
elif promedio >= 4:
    print("Debe rendir final")
else:
    print("Debe recursar")
