import ipaddress as ipaddress

#validate ipv4 address
print (ipaddress.ip_address(u'192.168.1.8'))

#validate ipv6 address
print (ipaddress.ip_address(u'FFFF:9999:2:FDE:257:0:2FAE:112D'))

#check the type of ip address
print(type(ipaddress.ip_address(u'192.168.0.255')))
print(type(ipaddress.ip_address(u'2001:db8::')))


#comparison of ip address

# Greater than,
print (ipaddress.IPv4Address(u'192.168.0.2') > ipaddress.IPv4Address(u'192.168.0.1'))
    
# Equality,
print (ipaddress.IPv4Address(u'192.168.0.2') == ipaddress.IPv4Address(u'192.168.0.1'))
    
# Inequality
print (ipaddress.IPv4Address(u'192.168.0.2') != ipaddress.IPv4Address(u'192.168.0.1'))


#address arithmetic

print (ipaddress.IPv4Address(u'192.168.0.2')+1)

print (ipaddress.IPv4Address(u'192.168.0.253')-3)

print (ipaddress.IPv4Address(u'192.168.10.253')+3)

