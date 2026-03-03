import json
from openpyxl import load_workbook

EXCEL_PATH = r"C:\Users\ENG-IBRAHIM\OneDrive\Desktop\الداودي\شركة الداودي كاملة.xlsx"

# عدّل هذا المسار إذا مشروعك بمكان ثاني
PROJECT_PATH = r"C:\Users\ENG-IBRAHIM\OneDrive\Desktop\ai-engibrahim"
OUT_JSON_PATH = PROJECT_PATH + r"\api.json"

wb = load_workbook(EXCEL_PATH, data_only=True)
ws = wb["API"]  # لازم اسم الشيت API

date_val = ws["A2"].value
total_val = ws["B2"].value
cars_val = ws["C2"].value  # إذا ما عندك C2 خليها فارغة بالـ Excel

data = {
    "date": str(date_val),
    "total": total_val,
    "cars": cars_val
}

with open(OUT_JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("✅ api.json updated:", data)