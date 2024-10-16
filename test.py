from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

# Função para fechar o aplicativo
def close_app():
    QApplication.quit()  # Encerra a aplicação

# Criação da aplicação
app = QApplication(sys.argv)

# Criação da janela principal
window = QMainWindow()
window.setWindowTitle("Meu Aplicativo")

# Criação do botão para fechar
button = QPushButton("Fechar", window)
button.clicked.connect(close_app)  # Conecta o botão à função close_app
button.resize(100, 40)  # Redimensiona o botão
button.move(50, 50)  # Move o botão para uma posição dentro da janela

# Define o tamanho da janela
window.setGeometry(100, 100, 200, 150)  # (x, y, largura, altura)

# Exibe a janela
window.show()

# Inicia o loop da aplicação
sys.exit(app.exec_())
