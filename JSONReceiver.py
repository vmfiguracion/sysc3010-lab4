# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import json

textport = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = ('localhost', port)
s.bind(server_address)

while True:

    print ("Waiting to receive on port %d : press Ctrl-C or Ctrl-Break to stop " % port)

    buf, address = s.recvfrom(port)
    values = json.loads(buf)
    print ("Received %s bytes from %s %s: " % (len(buf), address, buf ))

    for key in values.keys():
        print ('json[{}]={}'.format(key, values[key]))

s.shutdown(1)
