def ingresar_positivo():
    nota = int(input("Ingrese una nota: "))
    while (nota < 1 or nota > 10) and nota != -1:
        nota= int(input("Dato no válido! Ingrese una nota: "))
    return nota

def crear_lista():
    lista = []
    nota = ingresar_positivo()
    while nota != -1:
        lista.append(nota)
        nota = ingresar_positivo()
    return lista

def obtener_datos(lista):
    suma = 0
    cantidad_notas = len(lista)
    for i in range(cantidad_notas):
        suma = suma + lista[i]
    promedio = round(suma / cantidad_notas, 2)
    return promedio, cantidad_notas

# Programa principal
lista_notas = crear_lista()
prom, cant = obtener_datos(lista_notas)
print(f'Cantidad de notas: {cant}. Promedio: {prom} ')