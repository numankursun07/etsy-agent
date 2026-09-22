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
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# --------------------------------------------------
# FONT
# --------------------------------------------------

pdfmetrics.registerFont(
    TTFont("Arial", r"C:\Windows\Fonts\arial.ttf")
)

pdfmetrics.registerFont(
    TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf")
)

# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

OUTPUT_DIR = "product_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PDF_FILE = os.path.join(
    OUTPUT_DIR,
    "urban_jungle_plant_care_planner_en.pdf"
)

doc = SimpleDocTemplate(
    PDF_FILE,
    pagesize=A4,
    rightMargin=15 * mm,
    leftMargin=15 * mm,
    topMargin=15 * mm,
    bottomMargin=15 * mm
)

# --------------------------------------------------
# STYLES
# --------------------------------------------------

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "TitleCustom",
    parent=styles["Title"],
    fontName="Arial-Bold",
    alignment=TA_CENTER,
    fontSize=26,
    leading=32,
    spaceAfter=12
)

subtitle_style = ParagraphStyle(
    "SubtitleCustom",
    parent=styles["Normal"],
    fontName="Arial",
    alignment=TA_CENTER,
    fontSize=12,
    leading=18,
    spaceAfter=20
)

heading_style = ParagraphStyle(
    "HeadingCustom",
    parent=styles["Heading1"],
    fontName="Arial-Bold",
    fontSize=18,
    leading=22,
    spaceBefore=8,
    spaceAfter=12
)

small_style = ParagraphStyle(
    "SmallCustom",
    parent=styles["Normal"],
    fontName="Arial",
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
        "Botanical Care & Propagation Planner",
        subtitle_style
    )
)

story.append(
    Paragraph(
        "Plant Care, Light Mapping & Propagation Journal",
        subtitle_style
    )
)

story.append(Spacer(1, 25 * mm))

cover_data = [
    ["Plant Parent Name:", "____________________________"],
    ["Start Date:", "____________________________"],
    ["Collection Goal:", "____________________________"]
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

story.append(
    Paragraph(
        "BOTANICAL CONTROL CENTER",
        heading_style
    )
)

dashboard = [
    ["Section", "Quick Access"],
    ["01", "Plant Collection & Inventory"],
    ["02", "Light Mapping"],
    ["03", "Care & Watering Log"],
    ["04", "Propagation Journal"],
    ["05", "Plant Health Reference"],
    ["06", "Monthly Review"],
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
        ("FONTNAME", (0, 1), (-1, -1), "Arial"),
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
        "MONTHLY QUICK CHECK",
        heading_style
    )
)

quick = [
    ["Active Plants", "__________"],
    ["Plants in Propagation", "__________"],
    ["Plants Needing Attention", "__________"],
    ["Plants Due for Repotting", "__________"],
]

quick_table = Table(
    quick,
    colWidths=[80 * mm, 70 * mm]
)

quick_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Arial"),
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

story.append(
    Paragraph(
        "PLANT COLLECTION",
        heading_style
    )
)

inventory = [
    ["ID", "Plant", "Type", "Location", "Light", "Status"],
]

for number in range(1, 9):
    inventory.append([
        f"{number:02d}", "", "", "", "", ""
    ])

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
        ("FONTNAME", (0, 1), (-1, -1), "Arial"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ])
)

story.append(inventory_table)
story.append(PageBreak())

# --------------------------------------------------
# 4. PLANT CARE LOG
# --------------------------------------------------

story.append(
    Paragraph(
        "PLANT CARE LOG",
        heading_style
    )
)

care = [
    ["Date", "Plant", "Action", "Soil", "Observations"],
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
        ("FONTNAME", (0, 1), (-1, -1), "Arial"),
        ("FONTSIZE", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ])
)

story.append(care_table)
story.append(PageBreak())

# --------------------------------------------------
# 5. PROPAGATION JOURNAL
# --------------------------------------------------

story.append(
    Paragraph(
        "PROPAGATION JOURNAL",
        heading_style
    )
)

propagation_info = [
    ["Experiment No.:", "____________________________"],
    ["Mother Plant:", "____________________________"],
    ["Method:", "Water / Soil / Perlite / Sphagnum / Other"],
    ["Start Date:", "____________________________"],
    ["Last Check:", "____________________________"],
]

prop_table = Table(
    propagation_info,
    colWidths=[45 * mm, 105 * mm]
)

prop_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Arial"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
    ])
)

story.append(prop_table)
story.append(Spacer(1, 10 * mm))

milestones = [
    ["Stage", "Date", "Observation"],
    ["Start", "", ""],
    ["First Roots", "", ""],
    ["Growth", "", ""],
    ["Transfer to Soil", "", ""],
    ["Result", "", ""],
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
        ("FONTNAME", (0, 1), (-1, -1), "Arial"),
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

story.append(
    Paragraph(
        "LIGHT MAPPING",
        heading_style
    )
)

light_data = [
    ["Room", "Window Direction", "Morning", "Midday", "Evening", "Notes"],
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
        ("FONTNAME", (0, 1), (-1, -1), "Arial"),
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

story.append(
    Paragraph(
        "MONTHLY REVIEW",
        heading_style
    )
)

monthly = [
    ["Period", "____________________________"],
    ["Star Plants of the Month", "________________________________________"],
    ["Plants Needing Attention", "________________________________________"],
    ["Completed Care Tasks", "________________________________________"],
    ["Next Month Goal", "________________________________________"],
]

monthly_table = Table(
    monthly,
    colWidths=[55 * mm, 95 * mm]
)

monthly_table.setStyle(
    TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Arial"),
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
        "This planner is designed for general organization and plant-care tracking. "
        "It is not a substitute for professional horticultural advice.",
        small_style
    )
)

# --------------------------------------------------
# BUILD PDF
# --------------------------------------------------

doc.build(story)

print("PDF successfully created:")
print(PDF_FILE)