from matplotlib import pyplot
from openpyxl import workbook

file = 'plot.xlsx'
def gfx(x):
    return x.value

wb = Workbook()
ws = wb.active

ws[1] = 1

wb.save(file)

