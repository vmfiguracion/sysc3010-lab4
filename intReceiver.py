# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)
number_of_loops, address = s.recvfrom(port)

for i in range(int(number_of_loops.decode('utf-8'))):
   
    buf, address = s.recvfrom(port)
    
    print(str(buf.decode('utf-8')))
  
s.shutdown(1)
