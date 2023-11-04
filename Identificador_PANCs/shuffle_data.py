import os
import random
import shutil
import json

'''
todo:
* Permitir copiar os arquivos .txt das imagens que foram copiadas (lembre que os arquivos .txt tem o nome da classe e o id da foto da classe igual ao nome da foto)
* Fazer uma função que armazena em um arquivo .txt ou .json a quantidade de dados de treinamento, testes e validação de cada classe 
  Exemplo:
  calendula: {
    treinamento: 325,
    testes: 154,
    validacao: 40,
  },
  chicoria: {
    treinamento: 325,
    testes: 154,
    validacao: 40,
  },
'''

# Diretório raiz do seu dataset
dataset_root = 'dataset'

# Diretórios de treinamento, validação e teste
train_dir = os.path.join(dataset_root, 'train')
val_dir = os.path.join(dataset_root, 'validation')
test_dir = os.path.join(dataset_root, 'test')

# Taxas de divisão
train_ratio = 0.9
test_ratio = 0.1
val_ratio = 0.01

# Lista de classes (nomes dos diretórios de imagem)
classes = os.listdir(os.path.join(dataset_root, 'images'))
print(classes)

training_specs = {}

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
  # Calcula a taxa de validação 
  # 10% dos 90% de cada classe
  num_val = int(total_files * val_ratio)
  num_test = int(total_files - num_train - num_val)
  print(num_train, num_val, num_test)

  class_specs = {}
  class_specs["training"] = num_train
  class_specs["validation"] = num_val
  class_specs["testing"] = num_test
  training_specs[cls] = class_specs

  # Dividir os arquivos em conjuntos de treinamento, validação e teste
  train_files = img_files[:num_train]
  val_files = img_files[num_train:num_train + num_val]
  test_files = img_files[num_train + num_val:]
  print(len(train_files), len(val_files), len(test_files))
  # Criar diretórios de treinamento, validação e teste para a classe
  os.makedirs(os.path.join(train_dir, cls), exist_ok=True)
  os.makedirs(os.path.join(val_dir, cls), exist_ok=True)
  os.makedirs(os.path.join(test_dir, cls), exist_ok=True)

  # Cria um arquivo .txt com as quantidade de 

  # Copia os arquivos de imagem para os diretórios apropriados
  for img_file in train_files:
    shutil.copy(os.path.join(img_class_dir, img_file), os.path.join(train_dir, cls, img_file))
  for img_file in val_files:
    shutil.copy(os.path.join(img_class_dir, img_file), os.path.join(val_dir, cls, img_file))
  for img_file in test_files:
    shutil.copy(os.path.join(img_class_dir, img_file), os.path.join(test_dir, cls, img_file))

  # Copiar arquivos de anotação para os diretórios apropriados
  for ann_file in ann_files:
    shutil.copy(os.path.join(ann_class_dir, ann_file), os.path.join(train_dir, cls, ann_file))

with open("data.json", "w") as json_file:
  json.dump(training_specs, json_file, indent=4)
print("Concluído! As imagens e anotações foram divididas em conjuntos de treinamento, validação e teste.")
