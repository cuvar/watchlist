import xlsxwriter
import os

#https://xlsxwriter.readthedocs.io/tutorial02.html

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('watchlist.xlsx')
worksheet = workbook.add_worksheet()

file_stocks = open("aktien.txt","r+")
file_content = file_stocks.read()
stocks = file_content.split('\n')


worksheet.write(0, 0, 'Aktien')
worksheet.write(0, 1, 'Dividende')
worksheet.write(0, 2, 'Primär')
worksheet.write(0, 3, 'Sekundär')
worksheet.write(0, 4, 'Monate')
worksheet.write(0, 5, 'Einstieg')

# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0

# Iterate over the data and write it out row by row.
for item in (stocks):
    worksheet.write(row, col, item)
    row += 1

workbook.close()