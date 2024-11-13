import cv2
import numpy as np

# Carregar o classificador de faces e o reconhecedor treinado
classific = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor.read("classificadorEigen.yml")

# Carregar o dicionário de nomes para IDs
nome_para_id = np.load('nomes_ids.npy', allow_pickle=True).item()
id_para_nome = {v: k for k, v in nome_para_id.items()}  # Inverter o dicionário para obter nomes a partir de IDs

# Definir parâmetros para exibição
largura, altura = 220, 220

# Iniciar a captura de vídeo
camera = cv2.VideoCapture(0)

def reconhecer_nome():
    while True:
        conectado, imagem = camera.read()
        
        # Verifique se a captura foi bem-sucedida
        if not conectado or imagem is None:
            print("Erro ao capturar imagem da câmera.")
            break
        
        imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        facesdetec = classific.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

        for (x, y, l, a) in facesdetec:
            imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))

            # Realizar a previsão de reconhecimento facial
            id, confianca = reconhecedor.predict(imagemFace)

            # Obter o nome a partir do ID
            nome = id_para_nome.get(id, "Desconhecido")
            
            # Retorna o nome da pessoa reconhecida
            camera.release()
            cv2.destroyAllWindows()
            return nome

# Chama a função e imprime o nome reconhecido
nome_reconhecido = reconhecer_nome()
print("Nome reconhecido:", nome_reconhecido)
