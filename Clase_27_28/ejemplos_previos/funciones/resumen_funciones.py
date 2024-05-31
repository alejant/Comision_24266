# import random

# # Crear/Declarar una fx
# def mostrar_lista(lista):
#     for i in range(len(lista)):
#         print(lista[i], end= " ")
#     print()

# # Utilizar/Llamar/Invocar una fx
# numeros= [1,2,3,50,0,-34]
# palabras= ["A","KIWI","MANZANA"]
# mostrar_lista(numeros)
# mostrar_lista(palabras)

# # Cómo devolver un valor (return)
# def sumar_lista(lista):
#     suma= 0
#     for valor in lista:
#         suma+= valor
#     return suma # Devuelve/Retorna un valor

# print(sumar_lista(numeros))
# # print(sumar_lista())

# # ámbito/alcance de variables
# # print(suma) # NameError: name 'suma' is not defined
# # def sumar_lista(): # NO utilizar var globales

# # valores por defecto
# # def raiz(num):
# def raiz(num, r=2):
#     return num**(1/r)

# print(raiz(4)) # Se llaman luego de definirlas
# print(raiz(125,3)) # 5

# # to-do: crear un fx que crear una lista con valores aleatorios
# def crear_lista(N:int):
#     '''
#     pre: recibe N (el tamaño de la lista).
#     pos: devuelve una lista con valores al azar. 

#     '''
#     lista= []
#     for i in range(N):
#         lista.append(random.randint(1,100))
#     return lista

# numeros2= crear_lista(10)
# mostrar_lista(numeros2)
# help(crear_lista)



mi_lista =  [1, 2]
valor_extra = 10
suma = 5

# Cómo devolver un valor (return)
def sumar_lista(lista, extra):
    extra = 0
    # lista.clear()
    lista[0] = 2
    suma = 0
    for valor in lista:
        suma+= valor
    
    return suma + extra# Devuelve/Retorna un valor


resultado =  sumar_lista(extra=valor_extra, lista=mi_lista)

# sumar_lista([1, 2])
print(valor_extra)
print(mi_lista)


print(suma)