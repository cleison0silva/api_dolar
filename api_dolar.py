import requests

req = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
cotacao = req.json()

print("###Cotação do Dólar###\n")
print("Moeda: " + cotacao["USD"]["name"])
print("Data: " + cotacao["USD"]["create_date"])
print("Valor Atual: " + cotacao["USD"]["bid"])