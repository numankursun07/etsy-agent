import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
Sen bir Etsy dijital ürün araştırma asistanısın.

Gerçek Etsy satış verilerine erişimin olmadığını varsay.
Kesin olarak "en çok satan" veya "kesin trend" gibi iddialarda bulunma.

Bana 5 özgün dijital ürün fırsatı ver.

Her fırsat için:
- Ürün fikri
- Hedef müşteri
- Çözdüğü problem
- Ürün formatı
- Özgünleştirme fikri

Başka satıcıların ürünlerini kopyalama.
Türkçe ve kısa cevap ver.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

result = response.text

print(result)

with open("research_results.txt", "w", encoding="utf-8") as file:
    file.write(result)

print("\nAraştırma sonucu research_results.txt dosyasına kaydedildi.")