import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("product_plan.txt", "r", encoding="utf-8") as file:
    product_plan = file.read()

prompt = f"""
Sen bir Etsy listing hazırlama asistanısın.

Aşağıdaki ürün planını kullanarak Etsy için özgün bir ürün listeleme taslağı oluştur.

ÜRÜN PLANI:
{product_plan}

Şunları hazırla:

1. Etsy ürün başlığı
- Açık ve anlaşılır olsun.
- Ana ürünün ne olduğunu net şekilde anlatsın.
- Anahtar kelimeleri doğal şekilde kullan.
- Doğrulanmamış "en çok aranan" veya "yüksek hacimli" gibi iddialarda bulunma.

2. Ürün açıklaması
- İlk bölümde müşterinin problemini anlat.
- Daha sonra ürünün çözümünü anlat.
- İçeriği maddeler halinde açıkla.
- Dosya formatlarını belirt.
- Dijital ürün olduğunu ve fiziksel ürün gönderilmeyeceğini açıkça belirt.
- Kullanım şeklini anlat.

3. Etsy etiketleri
- En fazla 13 etiket oluştur.
- Her etiketi kısa ve alakalı tut.
- Ürünle doğrudan ilgili olmayan kelimeler kullanma.

4. Ürün kategorisi önerisi

5. Dijital dosya teslim listesi

6. 5 adet Etsy görseli için öneri
Her görsel için:
- Görselde ne gösterilmeli?
- Görsel üzerinde hangi kısa mesaj bulunmalı?

7. Müşteri SSS bölümü
En az 5 soru ve cevap oluştur.

8. Kalite kontrol listesi
Liste yayınlanmadan önce kontrol edilmesi gereken maddeleri yaz.

Başka satıcıların açıklamalarını veya ürünlerini kopyalama.
Özgün içerik oluştur.
Türkçe cevap ver.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

result = response.text

print(result)

with open("listing_plan.txt", "w", encoding="utf-8") as file:
    file.write(result)

print("\nListing planı listing_plan.txt dosyasına kaydedildi.")