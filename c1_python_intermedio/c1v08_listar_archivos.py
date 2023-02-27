import os


def listar_archivos(ruta):

    lista_archivos = os.listdir(ruta)
    return lista_archivos

ruta_absoluta = os.getcwd()
ruta_relativa = "01_python_intermedio/"
archivos = listar_archivos(ruta_relativa)
print(archivos)
