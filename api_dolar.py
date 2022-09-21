import requests

req = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
info = req.json()

moeda = info["USD"]["name"]
data = info["USD"]["create_date"]
cotacao = float(info["USD"]["bid"])

print("###Cotação do Dólar###\n")
print(f"Moeda: {moeda}")
print(f"Data: {data}")
print(f"Valor Atual: {cotacao:.2f}")