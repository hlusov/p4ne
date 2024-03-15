from random import randint as rand
from openpyxl import Workbook
import matplotlib.pyplot as plot

l, i = 0, 0
c = 500
l1 = []
def luck(): return {rand(1, c) for i in range(2)}
def num(): return {rand(1, c) for i in range(5)}

while i < 10000:
    if set(luck()) <= set(num()):
        l += 1
        l1.append(luck())
        if l >= 1000: break
    i += 1

print(l, i, luck(), num())
print(l1)