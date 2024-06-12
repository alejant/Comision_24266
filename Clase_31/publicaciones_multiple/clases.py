# Clase base Publicacion
class Publicacion:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def mostrar_info(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.año_publicacion}"

# Clase base Digital
class PublicacionDigital:
    def __init__(self, formato):
        self.formato = formato

    def mostrar_info(self):
        return f"Formato: {self.formato}"

# Clase derivada EBook
class EBook(Publicacion, PublicacionDigital):
    def __init__(self, titulo, autor, año_publicacion, formato, tamaño):
        Publicacion.__init__(self, titulo, autor, año_publicacion)
        PublicacionDigital.__init__(self, formato)
        self.tamaño = tamaño

    def mostrar_info(self):
        info_publicacion = Publicacion.mostrar_info(self)
        info_digital = PublicacionDigital.mostrar_info(self)
        return f"{info_publicacion}, {info_digital}, Tamaño: {self.tamaño}MB"

