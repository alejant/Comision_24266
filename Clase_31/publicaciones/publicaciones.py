from clases import Libro, LibroCientifico, Revista, Publicacion

# Ejemplo de uso
un_libro = Libro("Cien Años de Soledad", "Gabriel Garcia Marquez", 1967, "Novela")
un_libro_ciencia = LibroCientifico("Ciencia", "Alguien", 1967, "Novela", "Tesis")
una_revista = Revista("National Geographic", "Varios", 2023, 12)
otra_revista = Revista("Caras", "Varios", 2022, 30)


lista_publicaciones = [un_libro, una_revista, otra_revista, un_libro_ciencia]
otro_libro = Libro("La paciente silenciosa", "Alex Michaelides", 2019, "Thriller")

alguna_publicacion = Publicacion("La Publicación", "NN", "1910")

lista_publicaciones.append(otro_libro)
lista_publicaciones.append(alguna_publicacion)



print(un_libro.mostrar_info())
print(una_revista.mostrar_info())



def mostrar_publicaciones(publicaciones):
    for publicacion in publicaciones:
        if isinstance(publicacion, Publicacion):
            print(publicacion.mostrar_info())




mostrar_publicaciones(lista_publicaciones)