from Chatbot import GerarConteudo 
from Perguntas import InteracaoChatBot

while True:
    conversa = InteracaoChatBot()
    prompt = input(conversa.InteracaoRam())
    resposta = GerarConteudo(prompt)
    textogerado = resposta.gerar_texto()
    

    print(textogerado)

    confirmacao = input('Deseja continuar? ')
    entrada = ["não", "nao", "Não", "Nao"]

    result = confirmacao in entrada
   
    if result == True:
        despedida = InteracaoChatBot.despedida()
        print(despedida)
        break
    elif prompt == 'Sair' or prompt == 'sair':
        break
    else:
        continue