import requests

def obter_taxas():
    try:
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        response = requests.get(url)
        data = response.json()
        return data['rates']
    except Exception as e:
        print("Erro ao obter taxas de câmbio:", str(e))
        return None

def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    try:
        if moeda_origem == 'USD':
            taxa = taxas[moeda_destino]
        else:
            taxa_para_usd = taxas[moeda_origem]
            valor_em_usd = valor / taxa_para_usd
            taxa = taxas[moeda_destino]
            return valor_em_usd * taxa
        return valor * taxa
    except KeyError:
        return "Uma ou ambas as moedas não são válidas."

if __name__ == "__main__":
    print("Conversor de Moedas")
    
    taxas = obter_taxas()
    if taxas is None:
        exit()

    valor = float(input("Digite o valor a ser convertido: "))
    moeda_origem = input("Digite a moeda de origem (ex: USD, EUR, BRL): ").upper()
    moeda_destino = input("Digite a moeda de destino (ex: USD, EUR, BRL): ").upper()

    resultado = converter_moeda(valor, moeda_origem, moeda_destino, taxas)
    
    if isinstance(resultado, float):
        print(f"{valor} {moeda_origem} é igual a {resultado:.2f} {moeda_destino}")
    else:
        print(resultado)
