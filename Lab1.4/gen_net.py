import random, ipaddress
from openpyxl import Workbook

def gen_net():
    return ipaddress.IPv4Network((random.randint(int(ipaddress.IPv4Address('11.0.0.0')), int(ipaddress.IPv4Address('223.0.0.0'))), random.randint(8,24)), strict=False)

i, k = 0, 0
list_net = []

while i < 50:
    k += 1
    new_net = gen_net()
    if new_net.is_private:
        list_net.append(new_net)
        i += 1

list1 = sorted(list_net)
print(k, i, list_net)

wb = Workbook()
ws = wb.active

# ws.append(list_net)
#for i in len(list_net):
#    ws[]

wb.save('nets.xlsx')