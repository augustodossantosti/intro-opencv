""" Carregamento de imagens com opencv e exibição com matplotlib """

import cv2

def show_image(img):
  from matplotlib import pyplot as plt

  # Vetor para altura, largura e quantidade de canais de cor
  altura, largura, canais_cor = img.shape
  print(f"Dimensões da imagem: {largura} X {altura}")
  print(f"Canais de cor: {canais_cor}")

  # Converte a imagem de BGR para RGB
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  plt.imshow(img)
  plt.show()

def main():
  # Carrega a imagem
  abacate = cv2.imread("images/abacate.jpg")

  # Carrega a imagem em preto e branco
  laranja = cv2.imread("images/laranja.jpg", 0)

  show_image(abacate)

main()
