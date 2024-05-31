# Validaciones de datos
# a) DNI: Debe contener solamente números.
dni = input("Ingrese su DNI: ")
while not dni.isdigit(): # Se verifica si el DNI contiene solamente dígitos
     dni = input("Debe contener solamente números. Ingrese su DNI: ")

# b) Nombre: No puede tener más de 30 caracteres.
nombre = input("Ingrese su nombre: ")
while len(nombre) > 30: # Se verifica si el nombre tiene más de 30 caracteres
    nombre = input(f'{nombre}, su nombre es muy largo! ({len(nombre)}) Ingrese un nombre más corto: ')

#c) Apellido: Debe contener únicamente letras.
apellido = input("Ingrese su apellido: ")
while not apellido.isalpha() or ' ' in apellido: # Se verifica si el apellido contiene únicamente letras y no contiene espacios
    apellido = input("El apellido debe contener únicamente letras y no debe contener espacios. Ingrese su apellido: ")

#d)	Domicilio: Puede contener cualquier combinación de letras y números en la dirección de calle, pero en el número debe haber al menos un número presente y no tener caracteres alfabéticos.
domicilio_calle = input("Ingrese su domicilio (calle): ")
domicilio_numero = input("Ingrese su domicilio (numero): ")
digitos = 0
caracteres = 0

for caracter in domicilio_numero: # Se cuenta la cantidad de dígitos y caracteres alfabéticos en el número del domicilio
    if caracter.isdigit():
        digitos += 1
    if caracter.isalpha():
        caracteres += 1

while digitos == 0 or caracteres > 0:  # Se solicita al usuario ingresar un número de domicilio válido
    domicilio_numero = input("Debe contener al menos un número y no puede contener letras. Ingrese su domicilio (numero): ")
    digitos = 0
    caracteres = 0
    for caracter in domicilio_numero:
        if caracter.isdigit():
            digitos += 1
        if caracter.isalpha():
            caracteres += 1

# Datos para impresión
linea = "="*56
encab = ' universidad de python - datos del estudiante '
titulo = encab.title()
titulo_centrado = titulo.center(56, "=")
fecha = '31/10/2023'
fecha = fecha.rjust(56)

# Informe
print(fecha)
print(linea)
print(titulo_centrado)
print(linea)

usuario = dni.zfill(11)
print(f'ID: {usuario}')
print(f'NOMBRE COMPLETO: {apellido.upper()}, {nombre.title()}')
print(f'DOMICILIO: {domicilio_calle.upper()} {domicilio_numero}')
print(f'USUARIO: {apellido.lower()}-{nombre[0].lower()}{dni[:3]}')
nombres = nombre.split(' ')
print(f'CORREO ELECTRÓNICO: {apellido.lower()}.{nombres[0].lower()}@unipython.com.ar')
print(f'CONTRASEÑA: {apellido[0].upper()}{nombre[0].lower()}-{dni[-3:]}') # empezando desde el tercer dígito contando desde el final hasta el último caracter

leyenda = '''
Recomendamos cambiar su contraseña.
La presente información es confidencial.
Dpto. de Sistemas.
'''
print(leyenda)