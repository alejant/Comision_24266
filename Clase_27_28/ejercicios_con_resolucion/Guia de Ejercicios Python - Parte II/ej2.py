# a) Crear una lista llamada Materias que contendrá 3 materias (harcodeado). Mostrar en pantalla.
materias = ["Python I", "Bases de datos I", "Filosofía"]
print(materias)

# b) Agregar una materia al final y otra en la segunda posición. Mostrar en pantalla la lista, la posición de la primera materia y la posición de la última.
materias.append("Pseudocódigo")
materias.insert(1, "Python II")
print(f'Lista: {materias}')
print(f'Primera materia: {materias[0]}')
print(f'Última materia: {materias[len(materias)-1]}')

# c) Solicitar una materia por teclado. Verificar si existe y en caso de que no exista agregarla al final de la lista, recorrer la lista utilizando un bucle for. Mostrar la lista en pantalla y un mensaje de confirmación.
mat = input("Ingrese el nombre de la materia: ")
encontrado = False
for m in range(len(materias)):
    if materias[m].upper() == mat.upper():
        encontrado = True
if encontrado == False:
    materias.append(mat)
    print(f'Materia {mat} agregada.')
else:
    print(f'No es posible sumar la materia {mat}, ya existe.')
print(f'Lista actualizada: {materias}')

# d) Solicitar una materia por teclado y modificar su nombre por otro ingresado por teclado. Realizar la búsqueda verificando si la materia existe utilizando un bucle while. Mostrar la lista en pantalla y un mensaje de confirmación. 
mat = input("Ingrese el nombre de la materia a modificar: ")
nuevo_nombre = input("Ingrese el nuevo nombre para la materia: ")
encontrado = False
indice = 0
while indice < len(materias) and not encontrado:
    if materias[indice].upper() == mat.upper():
        encontrado = True
        materias[indice] = nuevo_nombre
    indice += 1
if encontrado:
    print(f'Materia {mat} modificada a {nuevo_nombre}.')
else:
    print(f'La materia {mat} no existe en la lista.')

# e) Solicitar una materia por teclado y eliminarla. Realizar la búsqueda verificando si la materia existe utilizando un bucle for - in. Mostrar la lista en pantalla sólo si la materia fue eliminada, junto con un mensaje de confirmación.
mat = input("Ingrese el nombre de la materia a eliminar: ")
encontrado = False

for materia in materias:
    if materia.upper() == mat.upper():
        materias.remove(materia)
        encontrado = True

if encontrado:
    print(f'Materia {mat} eliminada.')
    print(f'Lista actualizada de materias: {materias}')
else:
    print(f'La materia {mat} no existe en la lista.')

#f) Eliminar la última materia de la lista y la primera materia de la lista.
# Eliminar la última materia de la lista
if len(materias) > 0:
    ultima_materia = materias.pop()
    print(f'Se eliminó la última materia: {ultima_materia}')
else:
    print('No hay materias en la lista.')

# Eliminar la primera materia de la lista
if len(materias) > 0:
    primera_materia = materias.pop(0)
    print(f'Se eliminó la primera materia: {primera_materia}')
else:
    print('No hay materias en la lista.')

print(f'Lista actualizada de materias: {materias}')
