print("======================= Listado de aulas ======================")
print("Día\tAula")
cont = 1
while cont <= 6:
    if cont % 2 == 0:
        print(f'{cont}\tA-300')
    else:
        print(f'{cont}\tA-315')
    cont += 1 # cont = cont + 1

print()
print("====================== Carga de edades =========================")
carga_erronea = 0
edad = int(input("Ingrese una edad mayor o igual a 18: "))
while edad < 18:
    carga_erronea += 1 #Contador
    edad = int(input("Error! Ingrese una edad mayor o igual a 18: "))
print(f'La edad ingresada es: {edad}')
print(f'Se ha ingresado la edad erróneamente {carga_erronea} veces')

print()
print("====================== Promedio de notas =======================")
suma = 0
# Alternativa 1 - for i in range(fin):
for i in range(5):
    nota = int(input("Ingrese la nota: "))
    suma = suma + nota #Acumulador, alternativa: suma += nota
promedio = suma/(i+1)
print(f'El promedio de notas es: {promedio}')
# Alternativa 2 - for i in range(inicio, fin):
# for i in range(0,5):

# Alternativa 3 - for i in range(inicio, fin, paso):
# for i in range(0,5,1):

print()
print("====================== Costo del comedor =======================")

costo_diario = 1250
print("Dia\tCosto")
for i in range(6):
    print(f'{i+1}\t$ {(i+1)*costo_diario}')