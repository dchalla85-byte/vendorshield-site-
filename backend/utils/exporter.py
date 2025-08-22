import openpyxl
import os

def save_to_excel(filename: str, result: dict):
    path = "uploads/scan_history.xlsx"

    if not os.path.exists(path):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(["Filename", "Summary", "Flags"])
    else:
        wb = openpyxl.load_workbook(path)
        ws = wb.active

    flags_joined = "; ".join([f"{f['line']} ({f['reason']})" for f in result["flags"]])
    ws.append([filename, result["summary"], flags_joined])
    wb.save(path)
