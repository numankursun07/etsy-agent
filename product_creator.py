import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("product_plan.txt", "r", encoding="utf-8") as file:
    product_plan = file.read()

prompt = f"""
Sen bir dijital ürün içerik üretim asistanısın.

Aşağıdaki ürün planını kullanarak "Urban Jungle Ev Bitkileri Bakım ve Çoğaltma Günlüğü"
adlı dijital ürünün içerik taslağını oluştur.

ÜRÜN PLANI:
{product_plan}

Ürün şu bölümlerden oluşmalı:

1. COVER
- Ürün adı
- Kısa alt başlık
- Kullanıcı adı alanı

2. DASHBOARD
- Ana menü
- Bitki koleksiyonu
- Bakım takvimi
- Sulama takibi
- Gübreleme takibi
- Çoğaltma günlüğü
- Hastalık teşhis rehberi
- Gün ışığı haritası

3. PLANT COLLECTION
Her bitki için:
- Bitki adı
- Tür
- Konum
- Işık ihtiyacı
- Sulama sıklığı
- Son sulama
- Son gübreleme
- Notlar

4. PLANT CARE LOG
- Tarih
- Bitki
- Yapılan bakım
- Sulama
- Gübreleme
- Budama
- Notlar

5. PROPAGATION LOG
- Bitki
- Çoğaltma yöntemi
- Başlangıç tarihi
- Ortam
- Köklenme durumu
- Sonraki kontrol
- Sonuç
- Notlar

6. LIGHT MAPPING
- Oda adı
- Pencere yönü
- Günlük ışık süresi
- Işık seviyesi
- Bu bölgeye uygun bitkiler

7. PLANT HEALTH GUIDE
Yaygın problemler için:
- Problem adı
- Belirti
- Olası neden
- Genel çözüm önerisi
- Ne zaman uzman desteği düşünülmeli?

8. MONTHLY REVIEW
- Bu ay en iyi gelişen bitkiler
- Sorun yaşayan bitkiler
- Yapılan bakım
- Gelecek ay hedefleri

Her bölüm için kullanılabilecek gerçek metinleri ve tablo alanlarını üret.

ÖNEMLİ:
- Tıbbi veya bilimsel kesinlik iddiasında bulunma.
- Bitki hastalıklarında belirsizliği belirt.
- Başka satıcıların içeriklerini kopyalama.
- Özgün içerik oluştur.
- İçeriği daha sonra PDF/Canva/InDesign gibi araçlarla tasarlanabilecek şekilde düzenli ver.

Türkçe cevap ver.
"""

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

result = response.text

print(result)

os.makedirs("product_content", exist_ok=True)

with open("product_content/product_content.txt", "w", encoding="utf-8") as file:
    file.write(result)

print("\nÜrün içerikleri product_content/product_content.txt dosyasına kaydedildi.")