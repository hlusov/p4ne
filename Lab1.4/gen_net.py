import random, ipaddress
from openpyxl import Workbook
import matplotlib.pyplot as plot

def gen_net():
    return ipaddress.IPv4Network((random.randint(int(ipaddress.IPv4Address('11.0.0.0')), int(ipaddress.IPv4Address('223.0.0.0'))), random.randint(8,24)), strict=False)

i, k = 0, 0
list_net = []
graf = []
n = 1
for k in range (n):
    i = 0
    while i < 50:
        k += 1
        new_net = gen_net()
        if not new_net.is_private:
            list_net.append(new_net)
            i += 1
    graf.append(k)

list1 = sorted(list_net)
list2 = list(map(str, list1))
print(k, i, list_net)
print (graf)
wb = Workbook()
ws = wb.active

plot.plot (range(n),graf)
# plot.show()
ws.append(list2)
#for i in len(list_net):
#    ws[]

wb.save('nets.xlsx')