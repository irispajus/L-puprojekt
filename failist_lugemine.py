import openpyxl

exceli_asukoht_PCs = 'C:/Users/irispajus/Desktop/PY/loend.xlsx'

workbook = openpyxl.load_workbook(exceli_asukoht_PCs)
worksheet = workbook.active

lahtri_vaartus = worksheet['A1'].value
print(lahtri_vaartus)




