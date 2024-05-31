def sumar_numeros(num1, num2):
    ''' Recibir 2 números y sumarlos '''
    suma= num1+num2
    return suma # Retornar (devolver) un valor

def sumar_lista(lista):
    suma= 0
    for elem in lista:
        suma= suma+elem
    return suma

def calcular_sumatoria_prom(lista):
    """
    pre: recibe una lista.
    pos: devuelve la sumatoria y su promedio

    """
    suma= sumar_lista(lista)
    prom= suma/len(lista)

    return suma, prom # Retorno 2 valores

def raiz(num): # Ejemplo de uso de Valores por omisión
    '''
    pre: recibe un número y calcula su raiz (si sólo recibe num, calcula la raiz cuadrada).
    pos: devuelve la raíz del número.
    '''

# Prog Ppal
# resultado= sumar_numeros(10,5)
# print(resultado)
numeros= [1,2,4,-2]
# print(sumar_lista(numeros))
result1, result2= calcular_sumatoria_prom(numeros)
print("Suma:", result1, "Promedio:", result2)
