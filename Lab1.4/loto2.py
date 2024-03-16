from random import randint as rand
from matplotlib import pyplot

l = 0
c = 36
d = 100000
l1 = []
luck = lambda: {rand(1, c) for i in range(1)}
num = lambda: {rand(1, c) for i in range(1)}

for i in range(d):
    while not luck().issubset(num()):
        if l >= 10000: break
        l += 1
    l1.append(l); l=0
#print(l1)
pyplot.plot(list(range(d)), l1, 'ro')
pyplot.show()