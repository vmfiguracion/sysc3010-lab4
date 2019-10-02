# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, random

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)
n = int(input("Enter a number: "))

s.sendto(bytearray(str(n).encode('ascii')), server_address)

while n > 0:
    n_int = random.randint(0,10)
    
    
    s.sendto(bytearray(str(n_int).encode('ascii')), server_address)
    
    print (str(n_int));
    n -= 1

s.shutdown(1)

