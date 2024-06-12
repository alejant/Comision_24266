from abc import ABC, abstractmethod

# Clase abstracta
class Publicacion(ABC):
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    @abstractmethod
    def mostrar_info(self):
        pass

    def mostrar_titulo(self):
        print(f"El titulo es {self.titulo}")


# Clase concreta Libro
class Libro(Publicacion):
    def __init__(self, titulo, autor, año_publicacion, genero):
        super().__init__(titulo, autor, año_publicacion)
        self.genero = genero

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}, Genero: {self.genero}"

# Clase concreta Revista
class Revista(Publicacion):
    def __init__(self, titulo, autor, año_publicacion, numero_edicion):
        super().__init__(titulo, autor, año_publicacion)
        self.numero_edicion = numero_edicion

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}, Número de Edición: {self.numero_edicion}"
