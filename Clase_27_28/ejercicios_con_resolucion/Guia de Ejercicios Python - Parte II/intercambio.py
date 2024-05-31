# Modificar valores por posición
provincias = ["Mendoza", "Jujuy", "Salta"]
print(provincias) # Original
provincias[2]="Córdoba"
print(provincias) # Cambiada

# Intercambiar valores
aux = provincias[0]
provincias[0] = provincias[2]
provincias[2] = aux
print(provincias)
print()
