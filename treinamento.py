import cv2
import os
import numpy as np

# Inicialize o EigenFaceRecognizer
eigeface = cv2.face.EigenFaceRecognizer_create(num_components=50)

def getImagensComId():
    # Caminho das imagens na pasta 'fotos'
    caminhos = [os.path.join('fotos', f) for f in os.listdir('fotos')]
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        # Converte a imagem para escala de cinza
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        
        # Extrai o nome da pessoa do nome do arquivo (antes do primeiro ponto)
        nome = os.path.split(caminhoImagem)[-1].split('.')[0]
        
        # Adiciona o nome como ID
        ids.append(nome)
        faces.append(imagemFace)
        
    return ids, faces

# Obter as imagens e IDs
ids, faces = getImagensComId()
print("Treinando...")

# Convertendo IDs para um array de inteiros (necessário para o OpenCV)
# Crie um dicionário para associar cada nome a um identificador numérico
nome_para_id = {nome: idx for idx, nome in enumerate(set(ids))}
ids_num = np.array([nome_para_id[nome] for nome in ids])

# Treine o modelo usando os IDs numéricos
eigeface.train(faces, ids_num)
eigeface.write('classificadorEigen.yml')

print("Treinamento realizado!")

# Salve o dicionário de nomes para IDs para uso posterior
np.save('nomes_ids.npy', nome_para_id)