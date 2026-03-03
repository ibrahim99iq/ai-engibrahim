import os
from datetime import datetime, timedelta
import win32com.client as win32

# ======== الإعدادات ========

EXCEL_PATH = r"C:\Users\ENG-IBRAHIM\OneDrive\Desktop\الداودي\شركة الداودي كاملة.xlsx"
SHEET_NAME = "تقرير كلي"
DATE_CELL = "B3"

OUTPUT_FOLDER = r"C:\Users\ENG-IBRAHIM\OneDrive\Desktop\ai-engibrahim\history_images"

START_DATE = datetime(2025, 7, 1).date()
END_DATE = datetime(2026, 3, 3).date()

# ===========================

def main():

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    excel = win32.Dispatch("Excel.Application")
    excel.Visible = False
    excel.DisplayAlerts = False

    wb = excel.Workbooks.Open(EXCEL_PATH)
    ws = wb.Worksheets(SHEET_NAME)

    original_date = ws.Range(DATE_CELL).Value

    # خزّن PrintArea الأصلي
    original_print_area = ws.PageSetup.PrintArea

    current_date = START_DATE

    while current_date <= END_DATE:

        formatted_date = current_date.strftime("%Y-%m-%d")
        output_path = os.path.join(OUTPUT_FOLDER, f"{formatted_date}.pdf")

        print(f"Generating PDF: {formatted_date}")

        # غيّر التاريخ
        ws.Range(DATE_CELL).Value = current_date.strftime("%m/%d/%Y")
        excel.CalculateFullRebuild()

        # هنا نجبره يطبع فقط النطاق المحدد باسم info_tbl
        ws.PageSetup.PrintArea = ws.Range("info_tbl").Address

        ws.ExportAsFixedFormat(
            Type=0,
            Filename=output_path,
            Quality=0,
            IncludeDocProperties=True,
            IgnorePrintAreas=False,
            OpenAfterPublish=False
        )

        current_date += timedelta(days=1)

    # رجّع كلشي مثل ما كان
    ws.Range(DATE_CELL).Value = original_date
    ws.PageSetup.PrintArea = original_print_area

    wb.Save()
    wb.Close(SaveChanges=True)
    excel.Quit()

    print("✅ All PDFs generated correctly from info_tbl.")

if __name__ == "__main__":
    main()