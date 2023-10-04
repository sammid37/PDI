from PIL import Image
import numpy as np
import os
# import data_argumentation

# Definindo diretórios do dataset
folders = []

# Navegando pelos arquivos dos diretórios
for folder in folders:
  os.chdir(os.path.join(os.getcwd(),f'{folder}'))
  path = os.getcwd()
  files = os.listdir(path)

  # Abrindo as imagens no espaço de cor RGB
  for file in files:
    image = Image.open(path + "\\" + str(file))
    image = image.convert("RGB")
  os.chdir("..")