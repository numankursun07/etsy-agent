import requests

response = requests.get("https://www.etsy.com", timeout=10)

print("Durum kodu:", response.status_code)
print("Etsy'ye bağlandık!")