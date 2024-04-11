print("\n Importação e uso de modulo de terceiros")
import requests

url = "https://www.example.com"
response = requests.get(url)
print(f"soliciração http para {url} retornou o status {response.status_code}")