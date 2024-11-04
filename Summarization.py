import google.generativeai as genai
import os

class GerarResumo:
    def __init__(self, entrada):
        self.entrada = entrada
        api_key = os.getenv('API_KEY')
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def gerar_resumo(self):
        # Gera o resumo com o modelo Gemini
        response = self.model.generate_text(
            prompt=f"Please provide a short and concise summary of the following text:\n\n{self.entrada}",
            max_output_tokens=200,  # Ajuste para o tamanho do resumo desejado
            temperature=0.5  # Ajuste a temperatura conforme necessário
        )
        return response.result

texto = """"The Last of Us" é um aclamado jogo de ação e aventura desenvolvido pela Naughty Dog, lançado originalmente em 2013. Ambientado em um mundo pós-apocalíptico devastado por uma infecção fúngica que transforma pessoas em monstros, o jogo segue a jornada de Joel, um sobrevivente endurecido, e Ellie, uma adolescente imune à infecção. A narrativa se destaca pela profundidade emocional, explorando temas como perda, amor e a luta pela sobrevivência em um mundo implacável.

Os gráficos são impressionantes, com uma atenção meticulosa aos detalhes que trazem vida às paisagens desoladas e aos personagens complexos. A jogabilidade combina elementos de stealth, combate e resolução de quebra-cabeças, proporcionando uma experiência intensa e imersiva. A relação entre Joel e Ellie é central para a história, evoluindo de um vínculo relutante para um laço profundo e significativo.

A trilha sonora, composta por Gustavo Santaolalla, complementa perfeitamente o tom melancólico do jogo. "The Last of Us" não é apenas um jogo sobre sobrevivência; é uma reflexão sobre a humanidade em tempos de desespero. Seu sucesso gerou uma sequência, "The Last of Us Part II", que continuou a explorar as consequências das escolhas feitas pelos personagens. A franquia é amplamente considerada uma das melhores da história dos videogames, conquistando prêmios e uma base de fãs apaixonada."""

gerador_resumo = GerarResumo(texto)
resumo = gerador_resumo.gerar_resumo()
print("Resumo:", resumo)