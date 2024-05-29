

variable_1 = 33
variable_2 = 33

resultado = variable_1 + variable_2
resultado_string = str(resultado)

def mostrar_hola_mundo():
    saludo = "hola mundo"
    print(saludo)
    
mostrar_hola_mundo()
mostrar_hola_mundo()
mostrar_hola_mundo()


def super_calculo(numero_1, numero_2):
    '''
    El super calculo hace un calculo re zarpado
    retorna un super resultado
    '''
    if numero_1 is None:
        numero_1 = 0

    # Alto comentario
    resultado = numero_1 + numero_2
    return resultado



persona_edad = None
envejecimiento = 3

variable_loca = super_calculo(2, 3)

if persona_edad is None:
    persona_edad = 41
elif persona_edad is str:
    persona_edad = 99
else:
    persona_edad = 44


numero_encontrado = False
numero = 0

while not numero_encontrado:
    if numero == 3:
        numero_encontrado = True

    numero = numero + 1

for indice in range(4):
    print(indice)

variable_loca = super_calculo(persona_edad, envejecimiento)



valor_verdad = False

if valor_verdad:
    print("la verdad ha llegado")

print("El resultado es " + str(variable_loca))

print(resultado_string)
print("chau mundo")

