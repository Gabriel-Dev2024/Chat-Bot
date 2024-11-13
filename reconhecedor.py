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
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

# Iniciar a captura de vídeo
camera = cv2.VideoCapture(0)

while True:
    conectado, imagem = camera.read()
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesdetec = classific.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(150, 150))

    for (x, y, l, a) in facesdetec:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

        # Realizar a previsão de reconhecimento facial
        id, confianca = reconhecedor.predict(imagemFace)
        
        # Obter o nome a partir do ID
        nome = id_para_nome.get(id, "Desconhecido")
        
        # Exibir o nome abaixo do retângulo
        cv2.putText(imagem, nome, (x, y + a + 30), font, 2, (0, 0, 255), 2)
    
    cv2.imshow("Face", imagem)
    
    # Encerrar o loop com a tecla 'q'
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
