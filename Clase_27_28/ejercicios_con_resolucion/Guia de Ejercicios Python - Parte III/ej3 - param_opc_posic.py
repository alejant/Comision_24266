# Parámetros opcionales y parámetros posicionales
from datetime import datetime
anio_actual = datetime.now().year # Obtener el año actual

def registrar_datos(nomcomp, sede='Buenos Aires', anio=anio_actual):
    print(f'Se ha inscripto a {nomcomp.title()} en la sede {sede} para el año {anio}')

def datos_sede(direccion, ciudad, provincia='Buenos Aires'):
    print(f'Universidad de Python - {direccion} - {ciudad} - {provincia}')

# Programa principal

# Parámetros opcionales
registrar_datos("agustina gonzález","Córdoba",2021)
registrar_datos("diego lópez","Misiones")
registrar_datos("ANA FERNÁNDEZ")

# Parámetros posicionales
datos_sede("Av. Las Heras 3456", "Godoy Cruz", "Mendoza")
datos_sede(provincia='Chubut', ciudad='Rawson', direccion='Belgrano 312')
datos_sede(ciudad='Mar del plata', direccion='Av. Moreno 56')