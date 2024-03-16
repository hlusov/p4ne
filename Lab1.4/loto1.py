from random import randint as rand

cnt = 0
c = 100
def loto():
    global cnt
    cnt += 1
    luck = {rand(1, c) for i in range(2)}
    num = {rand(1, c) for i in range(5)}
    if luck.issubset(num):
        return print (cnt, luck, num)
    else: loto()

loto()