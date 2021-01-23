import socket
from colorama import init , Fore

#declaring colours for output
init()
GREEN = Fore.GREEN
RED = Fore.RED
WHITE = Fore.WHITE
BLUE = Fore.BLUE
YELLOW =  Fore.YELLOW

def port_check(host,port):
    try: #trying to connect to the port                     
        s = socket.socket()
        s.connect((host,port))
    except: #error message will be prompted if the connection is failed
        print(f"{WHITE}The HOST {YELLOW}{host} {WHITE}is {RED}closed {WHITE}in the port {YELLOW}{port}" , end="\r")
    else: #so if there is no error the port is open
        print(f"{WHITE}The HOST {YELLOW}{host} {WHITE}is {GREEN}opened {WHITE}in the port {YELLOW}{port}")
    s.close()
    
host = input(f"{BLUE}Enter the target's ip address\t:\t{RED}")

#total of 65535 ports

for ports in range(1, 65536):
    port_check(host,ports)

    


