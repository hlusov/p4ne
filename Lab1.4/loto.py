from random import randint as rand
from openpyxl import Workbook
import matplotlib.pyplot as plot

l, i = 0, 0
c = 1000
luck = {1}
num = {2}
while not luck.issubset(num):
    luck = {rand(1, c) for i in range(4)}
    num = {rand(1, c) for i in range(25)}
    i += 1
    if i > 10000000: break

print(i, luck, num)