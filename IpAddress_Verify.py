from ipaddress import ip_address, IPv4Address


def validIPAddress(IP: str) -> str:
    try:
        return True
    except ValueError:
        return False


ip_list = []
n = 10
for i in range(n):
    ip1 = input("Enter a valid IP address:")
    ip_list.append(ip1)

# bool_list = []
# for i in ip_list:
#     b = validIPAddress(i)
#     bool_list.append(b)

# print(bool_list)
# print(ip_list)
bin_list = []
oct_list = []
hex_list = []


for i in ip_list:
    if(validIPAddress(i) == True):

        bin_list.append('.'.join([bin(int(x)+256)[3:] for x in i.split('.')]))

        oct_list.append('.'.join(["%04o" % int(x) for x in i.split('.')]))

        hex_list.append('-'.join([hex(int(x)+256)[3:] for x in i.split('.')]))


with open('conversion.txt', 'w') as fp:
 
    for i in range(n):
        fp.write("\n\nDecimal data :")
        fp.write("\t%s" % ip_list[i])
        fp.write("\t\tBinary data :")
        fp.write("\t%s" % bin_list[i])
        fp.write("\t\t Octahedral data :")
        fp.write("\t%s" % oct_list[i])
        fp.write("\t\t Hexadecimal data :")
        fp.write("\t%s\n" % hex_list[i])

    # print("Done")
