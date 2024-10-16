import random
class InteracaoChatBot():
    def __init__(self):
        global iteracao
        iteracao = ["Olá! Como posso te ajudar hoje? ",
                    "No que posso ser útil? ",
                    "Qual o motivo da sua visita? ",
                    "O que você espera encontrar aqui? ",
                    "Qual a sua principal dúvida no momento? ",
                    'Bem-vindo! O que você gostaria de explorar hoje?',
                    'Oi! Pronto para adquirir novos conhecimentos?',
                    'Olá! Que assunto você gostaria de discutir?',
                    'Oi! Qual é a sua curiosidade de hoje?',
                    'Olá! Estou aqui para ajudar com suas perguntas!',
                    'Olá! O que você gostaria de aprender ou revisar?',
                    'Oi! Como posso ajudar a esclarecer suas dúvidas?',
                    'Olá! Estou aqui para ajudá-lo a crescer em seus estudos!',
                    'Olá! Quais são suas perguntas sobre o mundo do conhecimento?',
                    'Bem-vindo! Pronto para um pouco de conhecimento?'
                    ]
    def IteracaoRam(self):
        return random.choice(iteracao)