from PIL import Image
import numpy as np
import os

# Função para realizar data augmentation em uma imagem YOLO
def apply_data_augmentation(image_path, yolo_annotations, output_dir):
  # Carregue a imagem original
  original_image = Image.open(image_path)
  
  # Escala de cinza
  gray_image = original_image.convert('L')
  gray_image.save(os.path.join(output_dir, 'img_a_0001_bw.jpg'))
  
  # Flip horizontal
  flipped_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
  flipped_image.save(os.path.join(output_dir, 'img_a_0001_flip.jpg'))
  
  # Rotação de 30 graus
  rotated_image = original_image.rotate(30)
  rotated_image.save(os.path.join(output_dir, 'img_a_0001_rot.jpg'))
  
  # Atualize as anotações YOLO correspondentes
  # Você precisará ajustar as coordenadas das caixas delimitadoras nas anotações
  
  # Exemplo de como ajustar as anotações:
  for i in range(len(yolo_annotations)):
    # Supondo que as anotações estejam no formato (classe, x_center, y_center, largura, altura)
    _, x, y, w, h = yolo_annotations[i]
    # Ajuste as coordenadas para a nova imagem
    if i == 0:
      # Apenas uma caixa delimitadora no exemplo
      new_x, new_y = x, y  # Para a imagem em escala de cinza, não altere as coordenadas
      new_w, new_h = w, h
    elif i == 1:
      # Ajuste as coordenadas para a imagem espelhada (flip)
      new_x, new_y = original_image.width - x, y
      new_w, new_h = w, h
    else:
      # Ajuste as coordenadas para a imagem rotacionada
      new_x, new_y = x, y  # Apenas um exemplo simples, você pode ajustar a rotação de acordo com sua necessidade
      new_w, new_h = w, h
    
    # Atualize as coordenadas nas anotações
    yolo_annotations[i] = (yolo_annotations[i][0], new_x, new_y, new_w, new_h)

  return yolo_annotations

# Exemplo de uso
image_path = 'img_a_0001.jpg'
output_dir = 'data_augmentation_output'
yolo_annotations = [(0, 100, 100, 50, 50)]  # Exemplo de anotações

# Crie o diretório de saída se ele não existir
os.makedirs(output_dir, exist_ok=True)

# Realize data augmentation
new_annotations = apply_data_augmentation(image_path, yolo_annotations, output_dir)

# Salve as anotações atualizadas
with open(os.path.join(output_dir, 'img_a_0001.txt'), 'w') as f:
  for annotation in new_annotations:
    f.write(f"{annotation[0]} {annotation[1]} {annotation[2]} {annotation[3]} {annotation[4]}\n")
