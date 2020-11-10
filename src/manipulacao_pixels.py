""" Manipulação de imagem com opencv """

import numpy as np
import cv2

def show_image(img):
  from matplotlib import pyplot as plt

  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  plt.imshow(img)
  plt.show()

def get_color(img, y, x):
  return img.item(y, x, 0), img.item(y, x, 1), img.item(y, x, 2)

def set_color(img, y, x, b, g, r):
  img.itemset((y, x, 0), b)
  img.itemset((y, x, 1), g)
  img.itemset((y, x, 2), r)

def main():
  abacate = cv2.imread("images/abacate.jpg")

  altura, largura, canais_cor = abacate.shape

  for y in range(0, altura):
    for x in range(0, largura):

      # Exibe matriz com a cor (BGR) de cada pixel
      # print(f"[{x},{y}] = {abacate[y][x]}")
      # input()

      # Recupera as informaçãoes de cor
      azul, verde, vermelho = get_color(abacate, y, x)

      # Remove informações de vermelho e verde deixando a imagem na cor azul
      set_color(abacate, y, x, azul, 0, 0)

  # Escreve a imagem manipulada em disco
  cv2.imwrite("images/abacate_azul.jpg", abacate)

  #show_image(abacate)

main()
