import google.generativeai as genai
class GerarConteudo:
    def __init__(self, entrada):
        self.entrada = entrada
        genai.configure(api_key='AIzaSyBditdh8-JKnA7FkrDyGFicOf4xQOljePs')
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def gerar_texto(self):
        self.response = self.model.generate_content(
            self.entrada,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                stop_sequences=[""],
                max_output_tokens=2000,
                temperature=1.0,
            )
        )
        return self.response.text