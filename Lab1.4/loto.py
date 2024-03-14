from random import randint as rand
from openpyxl import Workbook
import matplotlib.pyplot as plot

l = 0
c = 1000000
len = 10

def luck(): return rand(1,c)

num = [rand(1,c) for i in range(len)]

while luck() not in num:
    l += 1
    if l > 1000000: break

print(l, luck(), num)