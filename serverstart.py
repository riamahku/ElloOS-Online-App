import sys
import socket

if len(sys.argv) == 3:
  ip = sys.argv[1]
  port = int(sys.argv[2])
else:
  print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >")
  exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (ip, port)
s.bind(server_address)
print("Do Ctrl+c to exit the server listen !!")
while True:
  print("####### Server is listening #######")
  data, address = s.recvfrom(4096)
  print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")
  send_data = input("Type some text to send => ")
  s.sendto(send_data.encode('utf-8'), address)
  print("\n\n 1. Server sent : ", send_data,"\n\n")
