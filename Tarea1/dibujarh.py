import cv2  # Not actually necessary if you just want to create an image.
import numpy as np
import matplotlib.pyplot as plt
import argparse
#from google.colab.patches import cv2_imshow


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--depth",
	help="path to input video", default = 3)
args = vars(ap.parse_args())
n = int(args["depth"])

def dibujar_H(imagen, centro, ancho, largo, grosor = 1):  
  x_1 = centro[0] - ancho // 2
  x_2 = centro[0] + ancho // 2 
  y_1 = centro[1] + largo // 2
  y_2 = centro[1] - largo // 2

  # Color en formato BGR 
  color = (0, 255, 0) 

  #Linea izquierda:
  imagen = cv2.line(imagen, (x_1 + 1, y_2), (x_1 + 1, y_1), grosor)

  #Linea derecha:
  imagen = cv2.line(imagen, (x_2 - 1, y_2), (x_2 - 1, y_1), grosor)

  #Linea media
  imagen = cv2.line(imagen, (x_1 + 1, centro[1]), (x_2 - 1, centro[1]), grosor)

  return(imagen)

def recursion(n, centro = None, imagen = None, m = None, r = 10):
  """
  n: entero, indica el nivel de H a dibujar
  centro: entero, coordendas (x,y) el centro de la H
  imagen: np.array, imagen que se va creando
  m : un contador que valida que se llego al final de árbol de H
  r : factor para que se aprecien mejor las imágenes
  """
  #Si n es igual a 0 se retorna NULL
  if n == 0:
    return(None)
  # Se inicializan las variables cuando se ejecuta la primera vez la función
  if centro is None and imagen is None and m is None:
    m = 1
    escala_tamanio = int(((1 - 2 ** (n + 1)) / (1 - 2)) - 2) * r
    #escala_tamanio = escala_tamanio if n == 1 else int(escala_tamanio * 2)
    # print(escala_tamanio)
    height, width = 2 * escala_tamanio + 10, 1 * escala_tamanio + 10
    # print("tamaños", height, width)
    # exponente = max(len(str(height)), len(str(width))) 
    imagen = np.zeros((height, width, 3), np.uint8) + 255
    centro = (width//2, height//2)
    # print("tamaños", height, width)
    # print(centro)
  # print("El valor de m", m)
  # print(centro)
  if m == n:
    # print("m == n")
    # print(m)
    # print( 2 * 2 ** (- m + 1) * r, 4 * 2 ** (- m + 1) * r)
    imagen = dibujar_H(imagen, centro, 2 * 2 ** (n - m) * r, 4 * 2 ** (n - m) * r)
    return imagen
  if m == 1:
    # print("m == 1")
    imagen = dibujar_H(imagen, centro, 2 * 2 ** (n - m) * r, 4 * 2 ** (n - m) * r)
    imagen = recursion(n, (centro[0] +  2 * 2 ** (n - m - 1) * r, centro[1] -  4 * 2 ** (n - m - 1) * r), imagen, m + 1, r)
    imagen = recursion(n, (centro[0] +  2 * 2 ** (n - m - 1) * r, centro[1] +  4 * 2 ** (n - m - 1) * r), imagen, m + 1, r)
    imagen = recursion(n, (centro[0] -  2 * 2 ** (n - m - 1) * r, centro[1] -  4 * 2 ** (n - m - 1) * r), imagen, m + 1, r)
    imagen = recursion(n, (centro[0] -  2 * 2 ** (n - m - 1) * r, centro[1] +  4 * 2 ** (n - m - 1) * r), imagen, m + 1, r)
    return imagen
  else:
    imagen = dibujar_H(imagen, centro, 2 * 2 ** (n - m) * r, 4 * 2 ** (n - m) * r)
    imagen = recursion(n, (centro[0] +  2 * 2 ** (n - m - 1) * r, centro[1] -  4 * 2 ** (n - m - 1) * r), imagen, m + 1, r)
    imagen = recursion(n, (centro[0] +  2 * 2 ** (n - m - 1) * r, centro[1] +  4 * 2 ** (n - m - 1) * r), imagen, m + 1, r)
    imagen = recursion(n, (centro[0] -  2 * 2 ** (n - m - 1) * r, centro[1] -  4 * 2 ** (n - m - 1) * r), imagen, m + 1, r)
    imagen = recursion(n, (centro[0] -  2 * 2 ** (n - m - 1) * r, centro[1] +  4 * 2 ** (n - m - 1) * r), imagen, m + 1, r)
    return imagen
    # recursion(n, image)
    # pass

respuesta = recursion(n)
plt.imshow(respuesta)
plt.savefig('H.png',  dpi=1000)





