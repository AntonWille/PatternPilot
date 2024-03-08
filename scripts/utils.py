import pandas as pd

# MaxQDA for some reason offers excel instead of csv for exports >.>
def convert_xlsx_to_csv(xlsx_file_path, csv_file_path):
    df = pd.read_excel(xlsx_file_path, sheet_name='Sheet1')
    df.to_csv(csv_file_path, index=False)
