# Clase base
class Publicacion:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}"
    
    def __str__(self) -> str:
        self.mostrar_info()


# Clase derivada Libro
class Libro(Publicacion):
    def __init__(self, titulo, autor, año_publicacion, genero):
        super().__init__(titulo, autor, año_publicacion)
        # Publicacion.__init__(self, titulo, autor, año_publicacion)
        self.genero = genero

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Genero: {self.genero}"
    
    def mostrar_genero(self):
        return f"Mi genero es {self.genero}"
    
# Clase derivada LibroCientifico
class LibroCientifico(Libro):
    def __init__(self, titulo, autor, año_publicacion, genero, tesis):
        super().__init__(titulo, autor, año_publicacion, genero)
        self.tesis = tesis


# Clase derivada Revista
class Revista(Publicacion):
    def __init__(self, titulo, autor, año_publicacion, numero_edicion):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_edicion = numero_edicion

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Número de Edición: {self.numero_edicion}"
    
    def mostrar_edicion(self):
        return f"Mi edicion es {self.numero_edicion}"
    

    
# una_publicacion = Publicacion("Publi 1", "Ale", 2023)
# un_libro = Libro("La paciente silenciosa", "Un loco", 2019, "Thriller")
# una_revista = Revista("Caras", "Autor", 2010, 5)
# un_libro_cientifico = LibroCientifico("Teorida de la Gravedad", "un loco", 2000, "Ciencia", "Cualquiera")


# valor_verdad = isinstance(un_libro_cientifico, LibroCientifico)
# valor_verdad = isinstance(un_libro_cientifico, Libro)
# valor_verdad = isinstance(un_libro_cientifico, Publicacion)
# valor_verdad = isinstance(un_libro_cientifico, Revista)



# valor_verdad = isinstance(una_publicacion, Publicacion)
# valor_verdad = isinstance(un_libro, Publicacion)
# valor_verdad = isinstance(una_revista, Publicacion)

# valor_verdad = isinstance(una_publicacion, Revista)
# valor_verdad = isinstance(un_libro, Revista)
# valor_verdad = isinstance(una_revista, Revista)

# print(una_publicacion.mostrar_info())
# print(un_libro.mostrar_info())
# print(una_revista.mostrar_info())
