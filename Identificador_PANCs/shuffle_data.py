import os
import random
import shutil

# Diretório raiz do seu dataset
dataset_root = '/Users/saman/OneDrive/Documentos/UFPB/PDI/Identificador_PANCs/dataset/'

# Diretórios de treinamento, validação e teste
train_dir = os.path.join(dataset_root, 'train')
val_dir = os.path.join(dataset_root, 'validation')
test_dir = os.path.join(dataset_root, 'test')

# Taxas de divisão
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Lista de classes (nomes dos diretórios de imagem)
classes = os.listdir(os.path.join(dataset_root, 'images'))
print(classes)

# Iterar sobre cada classe
for cls in classes:
  img_class_dir = os.path.join(dataset_root, 'images', cls)
  print(img_class_dir)
  ann_class_dir = os.path.join(dataset_root, 'annotations', cls)
  print(ann_class_dir)
  # Listar os arquivos de imagem e anotação
  img_files = os.listdir(img_class_dir)
  ann_files = os.listdir(ann_class_dir)

  # Embaralhar os arquivos
  random.shuffle(img_files)
  random.shuffle(ann_files)

  # Calcular os tamanhos de cada conjunto
  total_files = len(img_files)
  print(f"Total de arquivos em {cls}: {total_files}")
  num_train = int(total_files * train_ratio)
  num_val = int(total_files * val_ratio)
  num_test = total_files - num_train - num_val
  print(num_train, num_val, num_test)

  # Dividir os arquivos em conjuntos de treinamento, validação e teste
  train_files = img_files[:num_train]
  val_files = img_files[num_train:num_train + num_val]
  test_files = img_files[num_train + num_val:]
  print(len(train_files), len(val_files), len(test_files))
  # Criar diretórios de treinamento, validação e teste para a classe
  os.makedirs(os.path.join(train_dir, cls), exist_ok=True)
  os.makedirs(os.path.join(val_dir, cls), exist_ok=True)
  os.makedirs(os.path.join(test_dir, cls), exist_ok=True)

  # Copiar arquivos de imagem para os diretórios apropriados
  for img_file in train_files:
    shutil.copy(os.path.join(train_files, img_file), os.path.join(train_dir, cls, img_file))
  for img_file in val_files:
    shutil.copy(os.path.join(val_files, img_file), os.path.join(val_dir, cls, img_file))
  for img_file in test_files:
    shutil.copy(os.path.join(test_files, img_file), os.path.join(test_dir, cls, img_file))

  # Copiar arquivos de anotação para os diretórios apropriados
  for ann_file in ann_files:
    shutil.copy(os.path.join(ann_class_dir, ann_file), os.path.join(train_dir, cls, ann_file))

print("Concluído! As imagens e anotações foram divididas em conjuntos de treinamento, validação e teste.")
