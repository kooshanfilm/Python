import openpyxl as xl

ex_sheet = xl.load_workbook('Exp.xlsx')
sheet = ex_sheet['Home purchese']
print (sheet['F7'].value)
