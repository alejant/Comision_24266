from setuptools import setup
setup(
    name="paquete",
    version="0.2",
    description="Este es un paquete de ejemplo malisimo",
    author="Codo a Codo",
    author_email="io.codoacodo@bue.edu.ar",
    url="https://www.buenosaires.gob.ar/educacion/codo-codo",
    packages=['paquete','paquete.hola','paquete.adios'],
    scripts=[]
)
