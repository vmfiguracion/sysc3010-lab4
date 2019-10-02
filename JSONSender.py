# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time
import json

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

x = {
    "name": "John",
    "age": 30,
    "city": "new York"
}

for i in range(10):
    data = json.dumps(x)
    s.sendto(data.encode('utf-8'), server_address)
    
    time.sleep(1)
    x["age"] += 1

s.close()

