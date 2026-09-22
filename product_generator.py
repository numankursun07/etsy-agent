import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

prompt = """
Sen bir Etsy dijital ürün geliştirme asistanısın.

Aşağıdaki fırsatı kullanarak SATILABİLİR, ÖZGÜN bir dijital ürün tasarla.

FIRSAT:
Urban Jungle Ev Bitkileri Bakım ve Çoğaltma Günlüğü

Hedef müşteri:
Evinde çok sayıda bitki yetiştiren bitki ebeveynleri ve koleksiyonerler.

Çözdüğü problem:
Sulama, gübreleme ve bitki çoğaltma süreçlerini takip etme zorluğu.

Ürün formatı:
Digital Planner + Printable PDF.

Özgünleştirme fikirleri:
- Bitki hastalıkları için teşhis ve çözüm rehberi
- Odalara göre Gün Işığı Haritalama şablonu
- Sulama ve gübreleme takip sistemi
- Çoğaltma/propgation takip sayfası

Şunları oluştur:

1. Ürün adı
2. Hedef müşteri
3. Ürünün temel amacı
4. Ürün içinde bulunacak sayfalar
5. Her sayfanın kısa açıklaması
6. Ürünün özgün özellikleri
7. Dosya yapısı
8. Müşterinin ürünü nasıl kullanacağı
9. Etsy'de ürünün değer önerisi
10. Ürünü üretmek için adım adım üretim planı

Başka satıcıların ürünlerini kopyalama.
Mevcut ürünleri taklit etme.
Özgün bir ürün tasarla.

Türkçe ve düzenli cevap ver.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

result = response.text

print(result)

with open("product_plan.txt", "w", encoding="utf-8") as file:
    file.write(result)

print("\nÜrün planı product_plan.txt dosyasına kaydedildi.")