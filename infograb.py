
import os
import socket
from time import *

from colorama import  init, Back, Fore, Style
init(convert=True)
cammand = input(Fore.GREEN +"[+]ENTER THE COMMAND YOU TO EXECUTE\n")
if cammand == "ip":
 hostname = socket.gethostname()
 IPAddr = socket.gethostbyname(hostname)
print(f"The host name of this computer/machine is  {hostname}"  )
print(f"Your Computer IP Address is: {IPAddr} " )
#----------------------------------------------------------------------------------------------------------------------------------------------------------------

question = input("[+] press w to put information a file\n ")
if question == "w":

 f = open("info.txt", "a")

 f.write(f"\n Targeted machine name is {hostname},\n Targeted machine ipv4 is {IPAddr}")
 f.closed
else:
 print("file not made")

sleep(150)
#more thing will be added
