import google.generativeai as genai
import os
class GerarConteudo:
    def __init__(self, entrada):
        self.entrada = entrada
        api_key = os.getenv('API_KEY')
        genai.configure(api_key=api_key)
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