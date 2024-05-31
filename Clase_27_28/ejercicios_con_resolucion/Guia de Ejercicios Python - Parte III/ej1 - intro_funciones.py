# FUNCIONES EN PYTHON: Sintaxis básica

#Ejercicio 1
def imprimir_mensaje():
    print("=======================================")
    print("Bienvenidos a la Universidad de Python!")
    print("=======================================")

def imprimir_aulas():
    print("Piso\tAulas")
    for i in range(1,6):
        inicio = i*100
        fin = inicio+10
        print(f'{i}\t{inicio} a {fin}')

def imprimir_aulas_dos(): # Versión sin usar \t
    print(f'{"Piso":<10}{"Aulas":<10}')
    for i in range(1,6):
        inicio = i*100
        fin = inicio+10
        print(f'{i:<10}{inicio} a {fin}')

# Programa principal
imprimir_mensaje()
print()
imprimir_aulas()
print()
imprimir_aulas_dos()