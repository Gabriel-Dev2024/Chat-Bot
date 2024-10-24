import requests

def get_weather(city_name):
    api_key = "3a39e2cdfa1311ea17cbd95cc6595f37"  # Substitua pela sua chave da API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Monta a URL completa da requisição
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    
    # Faz a requisição HTTP para a API
    response = requests.get(complete_url)
    
    # Converte a resposta para JSON
    data = response.json()
    
    # Verifica se a resposta foi válida
    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temperature = main["temp"]
        return f"Em {city_name}, a temperatura é de {temperature}°C com {weather_desc}."
    else:
        return "Cidade não encontrada."

# Exemplo de uso
city = input("Digite o nome da cidade: ")
print(get_weather(city))
