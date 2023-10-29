import os

''' Configuração das anotações
  0: "calendula",
  1: "chicory",
  2: "daisy",
  3: "dandelion",
  4: "garlicmustard"
'''

#* Solicita o diretório que contém os arquivos .txt
txt_directory = '/Users/saman/OneDrive/Documentos/UFPB/PDI/Identificador_PANCs/dataset/garlicmustard_annotation/'

# Solicita o número inteiro a ser usado para substituir o primeiro elemento da linha
class_id_to_replace = int(input("Informe o número inteiro de 0 a 4 para substituir o primeiro elemento da linha: "))

# Verifica se o número fornecido está dentro do intervalo válido
if class_id_to_replace < 0 or class_id_to_replace > 4:
  print("Número fora do intervalo válido (0 a 4).")
else:
  # Verifica se o diretório existe
  if not os.path.exists(txt_directory):
    print(f"O diretório {txt_directory} não existe.")
  else:
    # Lista os arquivos .txt no diretório
    txt_files = [file for file in os.listdir(txt_directory) if file.endswith('.txt')]

    for txt_file in txt_files:
      # Lê o conteúdo do arquivo .txt original
      with open(os.path.join(txt_directory, txt_file), 'r') as original_file:
        lines = original_file.readlines()

      # Substitui o primeiro elemento da linha pelo número fornecido
      modified_lines = []
      for line in lines:
        elements = line.strip().split()
        elements[0] = str(class_id_to_replace)  # Substitui o primeiro elemento
        modified_line = ' '.join(elements) + '\n'
        modified_lines.append(modified_line)

      # Cria um novo arquivo .txt com o conteúdo modificado
      modified_file_path = os.path.join(txt_directory, txt_file)
      with open(modified_file_path, 'w') as modified_file:
        modified_file.writelines(modified_lines)

      print(f"Arquivo {txt_file} modificado com sucesso.")

print("Processamento concluído.")