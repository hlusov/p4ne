from openpyxl import Workbook as xl
import re, random
test_dir = 'C:\\Users\\laser\\Desktop\\'
testfile = 'py_xls.xls'

book = xl()
ws = book.active
color = str(hex(random.randint(0, 16777215)))[2:]
print (color)
ws.sheet_properties.tabColor = color

book.save(testfile)
