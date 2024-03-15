from random import randint as rand

count = 0
c = 10
def loto():
    luck = {rand(1, c) for i in range(2)}
    num = {rand(1, c) for i in range(5)}
    if luck <= num:
        return print (count, luck, num)
    else: count = 1; loto()

loto()