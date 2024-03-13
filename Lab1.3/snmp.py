from pysnmp.hlapi import *
# from ipaddress import *

engine = SnmpEngine()
community = CommunityData("public", mpModel=0)
transp = UdpTransportTarget(("10.31.70.209", "161"))
context_data = ContextData()

snmp_ver = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_int = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

# res = getCmd(engine, community, transp, context_data, ObjectType(snmp_ver), lexicographicMode=False)
res = nextCmd(engine, community, transp, context_data, ObjectType(snmp_int), lexicographicMode=False)

for r in res:
    print (r[3])
