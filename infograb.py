import os
import socket
import dns.reversename
from time import *
from netaddr import *
from colorama import Fore, Back, Style
cammand = input(Fore.GREEN +"[+] ENTER THE COMMAND YOU TO EXECUTE:\n")
if cammand == "ip":
 hostname = socket.gethostname()
 IPAddr = socket.gethostbyname(hostname)
print(f"The host name of this computer/machine is  {hostname}"  )
print(f"Your Computer IP Address is: {IPAddr} " )
ip = IPAddress(f'{IPAddr}').ipv6()
print(f"the Target Machine is ipv6 is{ip}")
domain = dns.reversename.from_address(f"{IPAddr}")
print(domain)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

question = input("[+] press w to put information a file:\n ")
if question == "w":

 f = open("info.txt", "a") #appends the fle/ file name is changeable
 print("file was made")

 f.write(f"\n Targeted machine name is {hostname},\n Targeted machine ipv4 is {IPAddr}, \n Targeted machine ipv6 is {ip}, \n The reverse dns name is {domain},\n  on Targeted machine") # write the date file
 f.closed
else:
 print("file was not made")

sleep(5)


