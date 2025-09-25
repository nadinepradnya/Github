import json
import pandas as pd

# --- Load JSON ---
with open("Nadine Pradnya_V3925011.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# --- Simpan ke Excel ---
output_file = "Data_JSON.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    for kategori, records in data.items():
        df = pd.DataFrame(records)
        df.to_excel(writer, sheet_name=kategori, index=False)

print(f"Data berhasil disimpan ke {output_file}")
