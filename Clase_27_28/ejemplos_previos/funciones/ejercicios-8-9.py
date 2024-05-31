'''
8) Escribe un programa que pida VARIOS númeroS y nos diga si es divisible 
por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro) 

9) Añadir al ejercicio anterior que nos diga por cuál de los cuatro es 
divisible (hay que decir todos por los que es divisible)

'''
# num= int(input("Ingrese un número: "))
# while num!=0:
#     if num%2==0 or num%3==0 or num%5==0 or num%7==0: # Divisible por 2
#         print("Es divisible por 2,3,5 o 7.")
#     num= int(input("Ingrese un número: "))
# print((-3)%2)

# 9)
num= int(input("Ingrese un número: "))
while num!=0:
    if num%2==0: # Divisible por 2
        print("Es divisible por 2.")
    if num%3==0: # Divisible por 3
        print("Es divisible por 3.")
    if num%5==0: # Divisible por 5
        print("Es divisible por 5.")
    if num%7==0: # Divisible por 7
        print("Es divisible por 7.")
    num= int(input("Ingrese un número: "))
