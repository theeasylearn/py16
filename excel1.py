import xlsxwriter

workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook._add_sheet('sheet1')

worksheet.write('B3','hello world ')
worksheet.write('B2','hello world 2')

workbook.close()