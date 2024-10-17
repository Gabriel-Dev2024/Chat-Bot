from Chatbot import GerarConteudo
from Perguntas import InteracaoChatBot

while True:
    conversa = InteracaoChatBot()
    prompt = input(conversa.InteracaoRam())
    resposta = GerarConteudo(prompt)
    textogerado = resposta.gerar_texto()

    print(textogerado)

    confirmacao = input('Deseja continuar? ')

    if confirmacao == 'Não' or confirmacao == 'não' or confirmacao == 'Nao' or confirmacao == 'nao':
        break
    elif prompt == 'Sair' or prompt == 'sair':
        break
    else:
        continue