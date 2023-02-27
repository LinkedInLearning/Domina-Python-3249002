import cv2
import os

from PIL import Image


def abrir_imagen_pilllow(ruta_absoluta_img):

    imagen = Image.open(ruta_absoluta_img)
    imagen.show()


def abrir_imagen_opencv(ruta_img):
    
    imagen = cv2.imread(ruta_img, cv2.IMREAD_COLOR)
    cv2.imshow("Papitas", imagen)
    cv2.waitKey(0)

ruta_relativa = "01_python_intermedio/papitas.jpg"
ruta_absoluta = os.path.join(os.getcwd(), ruta_relativa)

abrir_imagen_pilllow(ruta_absoluta)
abrir_imagen_opencv(ruta_relativa)
