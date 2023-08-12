import xlwings as xw

workbook = xw.Book('demo1.xlsx').sheets['sheet']

workbook.range('A10').value = "Param Patel"