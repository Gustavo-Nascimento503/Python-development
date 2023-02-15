import requests

def converter_real_para_outra_moeda(valor_real, moeda_destino):


    url = f"https://economia.awesomeapi.com.br/json/last/BRL-{moeda_destino}"
    response = requests.get(url)
    dados = response.json()


    cotacao = float(dados[f"BRL{moeda_destino}"]["ask"])
    valor_destino = valor_real * cotacao


    valor_destino_formatado = "{:.2f}".format(valor_destino)


    print(f"R${valor_real:.2f} equivale a {valor_destino_formatado} {moeda_destino}")


valor_real = float(input("Digite o valor em Real que deseja converter: R$"))
moeda_destino = input("Digite a moeda para a qual deseja converter (USD, EUR ou BTC): ")
converter_real_para_outra_moeda(valor_real, moeda_destino)


