import requests


cep = input("Digite o CEP desejado: ")
url = f"https://viacep.com.br/ws/{cep}/json/"


response = requests.get(url)


if response.status_code == 200:
    dados = response.json()
    print(f"CEP: {dados['cep']}")
    print(f"Logradouro: {dados['logradouro']}")
    print(f"Bairro: {dados['bairro']}")
    print(f"Cidade: {dados['localidade']}")
    print(f"Estado: {dados['uf']}")
else:
    print("CEP não encontrado.")
