from pysnmp.hlapi import *

eng = SnmpEngine()
community = CommData("public", mpmodel=0)
transp = UdpTransportTarget(("10.31.70.209", "161"))
context_data = ContextData()

snmp_ver = ObjectIdentity('SNMPv2-MIB', 'sysDescr'0)
snmp_interfaces = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

res = nextCmd(eng, community, transp, context_data, ObjectType(snmp_interfaces))
print(type(res))
print (res)