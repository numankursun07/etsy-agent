from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(
    TTFont("Arial", r"C:\Windows\Fonts\arial.ttf")
)
pdfmetrics.registerFont(
    TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf")
)	

OUTPUT_DIR = "product_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PDF_FILE = os.path.join(
    OUTPUT_DIR,
    "urban_jungle_plant_care_planner.pdf"
)

doc = SimpleDocTemplate(
    PDF_FILE,
    pagesize=A4,
    rightMargin=15 * mm,
    leftMargin=15 * mm,
    topMargin=15 * mm,
    bottomMargin=15 * mm
)

styles = getSampleStyleSheet()
styles["Normal"].fontName = "Arial"
styles["Title"].fontName = "Arial"
styles["Heading1"].fontName = "Arial"
styles["Heading2"].fontName = "Arial"

title_style = ParagraphStyle(
    "TitleCustom",
    parent=styles["Title"],
    alignment=TA_CENTER,
    fontSize=26,
    leading=32,
    spaceAfter=12
)

subtitle_style = ParagraphStyle(
    "SubtitleCustom",
    parent=styles["Normal"],
    alignment=TA_CENTER,
    fontSize=12,
    leading=18,
    spaceAfter=20
)

heading_style = ParagraphStyle(
    "HeadingCustom",
    parent=styles["Heading1"],
    fontSize=18,
    leading=22,
    spaceBefore=8,
    spaceAfter=12
)

body_style = ParagraphStyle(
    "BodyCustom",
    parent=styles["BodyText"],
    fontSize=9,
    leading=13,
    spaceAfter=6
)

small_style = ParagraphStyle(
    "SmallCustom",
    parent=styles["BodyText"],
    fontSize=7.5,
    leading=10
)

story = []

# --------------------------------------------------
# 1. COVER
# --------------------------------------------------

story.append(Spacer(1, 45 * mm))

story.append(
    Paragraph(
        "URBAN JUNGLE",
        title_style
    )
)

story.append(
    Paragraph(
        "Botanical Care & Propagation Lab",
        subtitle_style
    )
)

story.append(
    Paragraph(
        "Ev Bitkileri Bakım, Işık Haritalama ve Çoğaltma Günlüğü",
        subtitle_style
    )
)

story.append(Spacer(1, 25 * mm))

cover_data = [
    ["Bitki Ebeveyninin Adı:", "____________________________"],
    ["Başlangıç Tarihi:", "____________________________"],
    ["Koleksiyon Hedefi:", "____________________________"]
]

cover_table = Table(
    cover_data,
    colWidths=[55 * mm, 95 * mm]
)

cover_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("FONTNAME", (0, 0), (-1, -1), "Arial"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
    ])
)

story.append(cover_table)
story.append(PageBreak())

# --------------------------------------------------
# 2. DASHBOARD
# --------------------------------------------------

story.append(Paragraph("BOTANİK KONTROL MERKEZİ", heading_style))

dashboard = [
    ["Bölüm", "Hızlı Erişim"],
    ["01", "Bitki Koleksiyonu & Envanter"],
    ["02", "Gün Işığı Haritası"],
    ["03", "Bakım & Sulama Takvimi"],
    ["04", "Çoğaltma Günlüğü"],
    ["05", "Bitki Sağlığı Rehberi"],
    ["06", "Aylık Değerlendirme"],
]

table = Table(
    dashboard,
    colWidths=[25 * mm, 125 * mm]
)

table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Arial-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
    ])
)

story.append(table)
story.append(Spacer(1, 15 * mm))

story.append(
    Paragraph(
        "AYLIK HIZLI BAKIŞ",
        heading_style
    )
)

quick = [
    ["Aktif Bitki Sayısı", "__________"],
    ["Çoğaltma Aşamasındaki", "__________"],
    ["Takip Gerektiren", "__________"],
    ["Saksı Değişimi Gereken", "__________"],
]

quick_table = Table(
    quick,
    colWidths=[80 * mm, 70 * mm]
)

quick_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
    ])
)

story.append(quick_table)
story.append(PageBreak())

# --------------------------------------------------
# 3. PLANT COLLECTION
# --------------------------------------------------

story.append(Paragraph("BİTKİ KOLEKSİYONU", heading_style))

inventory = [
    ["ID", "Bitki", "Tür", "Konum", "Işık", "Durum"],
    ["01", "", "", "", "", ""],
    ["02", "", "", "", "", ""],
    ["03", "", "", "", "", ""],
    ["04", "", "", "", "", ""],
    ["05", "", "", "", "", ""],
    ["06", "", "", "", "", ""],
    ["07", "", "", "", "", ""],
    ["08", "", "", "", "", ""],
]

inventory_table = Table(
    inventory,
    colWidths=[
        10 * mm,
        32 * mm,
        32 * mm,
        28 * mm,
        28 * mm,
        25 * mm
    ],
    repeatRows=1
)

inventory_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Arial-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWHEIGHT", (0, 0), (-1, -1), 12),
    ])
)

story.append(inventory_table)
story.append(PageBreak())

# --------------------------------------------------
# 4. PLANT CARE LOG
# --------------------------------------------------

story.append(Paragraph("BAKIM TAKİP GÜNLÜĞÜ", heading_style))

care = [
    ["Tarih", "Bitki", "İşlem", "Toprak", "Gözlem"],
]

for _ in range(12):
    care.append(["", "", "", "", ""])

care_table = Table(
    care,
    colWidths=[
        23 * mm,
        32 * mm,
        38 * mm,
        27 * mm,
        40 * mm
    ],
    repeatRows=1
)

care_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Arial-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ])
)

story.append(care_table)
story.append(PageBreak())

# --------------------------------------------------
# 5. PROPAGATION
# --------------------------------------------------

story.append(Paragraph("ÇOĞALTMA GÜNLÜĞÜ", heading_style))

propagation_info = [
    ["Deney No:", "____________________________"],
    ["Ana Bitki:", "____________________________"],
    ["Yöntem:", "Su / Toprak / Perlit / Sphagnum / Diğer"],
    ["Başlangıç Tarihi:", "____________________________"],
    ["Son Kontrol:", "____________________________"],
]

prop_table = Table(
    propagation_info,
    colWidths=[45 * mm, 105 * mm]
)

prop_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
    ])
)

story.append(prop_table)
story.append(Spacer(1, 10 * mm))

milestones = [
    ["Aşama", "Tarih", "Gözlem"],
    ["Başlangıç", "", ""],
    ["İlk kök", "", ""],
    ["Gelişim", "", ""],
    ["Toprağa aktarım", "", ""],
    ["Sonuç", "", ""],
]

milestone_table = Table(
    milestones,
    colWidths=[50 * mm, 35 * mm, 65 * mm]
)

milestone_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Arial-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ])
)

story.append(milestone_table)
story.append(PageBreak())

# --------------------------------------------------
# 6. LIGHT MAPPING
# --------------------------------------------------

story.append(Paragraph("GÜN IŞIĞI HARİTASI", heading_style))

light_data = [
    ["Oda", "Pencere Yönü", "Sabah", "Öğle", "Akşam", "Notlar"],
]

for _ in range(8):
    light_data.append(["", "", "", "", "", ""])

light_table = Table(
    light_data,
    colWidths=[
        27 * mm,
        30 * mm,
        25 * mm,
        25 * mm,
        25 * mm,
        38 * mm
    ],
    repeatRows=1
)

light_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Arial-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ])
)

story.append(light_table)
story.append(PageBreak())

# --------------------------------------------------
# 7. MONTHLY REVIEW
# --------------------------------------------------

story.append(Paragraph("AYLIK BOTANİK DEĞERLENDİRME", heading_style))

monthly = [
    ["Dönem", "____________________________"],
    ["Ayın yıldız bitkileri", "________________________________________"],
    ["Zorlanan bitkiler", "________________________________________"],
    ["Tamamlanan bakım", "________________________________________"],
    ["Gelecek ay hedefi", "________________________________________"],
]

monthly_table = Table(
    monthly,
    colWidths=[55 * mm, 95 * mm]
)

monthly_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ])
)

story.append(monthly_table)

story.append(Spacer(1, 15 * mm))

story.append(
    Paragraph(
        "Not: Bu planner genel organizasyon ve takip amacıyla hazırlanmıştır. "
        "Bitki sağlığıyla ilgili sorunlarda güvenilir bir bitki uzmanından "
        "profesyonel destek alınması önerilir.",
        small_style
    )
)

# --------------------------------------------------
# BUILD PDF
# --------------------------------------------------

doc.build(story)

print("PDF başarıyla oluşturuldu:")
print(PDF_FILE)