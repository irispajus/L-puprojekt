import openpyxl

exceli_asukoht_PCs = 'C:/Users/irispajus/Desktop/PY/loend.xlsx'

workbook = openpyxl.load_workbook(exceli_asukoht_PCs)
worksheet = workbook.active
tulpade_arv = worksheet.max_column

for i in range(1, tulpade_arv + 1):
  lahter = worksheet.cell(row = 1, column = i)
  print(lahter.value)




