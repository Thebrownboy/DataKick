import pandas as pd
df1 = pd.read_csv('./matches_shots_out.csv')
df2 = pd.read_csv('./possession_out.csv')
df = pd.merge(df1, df2, left_index=True, right_index=True)
df = df.drop(columns=['Result_x'])
df = df.rename(columns={'Result_y': 'Result'})
df.to_csv('./matches_shots_possession.csv', index=False)
print(df.shape)
print(df.head())
# turn csv to xlsx
import csv
import xlsxwriter
with open('./matches_shots_possession.csv', 'r') as csv_file:
    workbook = xlsxwriter.Workbook('./matches_shots_possession.xlsx')
    worksheet = workbook.add_worksheet()
    reader = csv.reader(csv_file)
    for r, row in enumerate(reader):
        for c, col in enumerate(row):
            worksheet.write(r, c, col)
    workbook.close()