import os,sys,time,socket,threading
print("Please wait running fastboot...")

HEADER = 64
PORT = 1222
SERVER = socket.gethostbyname(socket.gethostname())
ADDR64 = (SERVER, PORT)
FORMAT = 'utf-8'
dc_msg = "Terminal disconnected"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR64)

def handle_client(conn, addr):
    print(f"[WIFI_TERMINAL_CONNECTION_NEW] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
          msg_length = int(msg_length)
          msg = conn.recv(msg_length).decode(FORMAT)
          if msg == dc_msg:
              connected = False

          print(f"[{addr}] {msg}")
          if msg == dc_msg:
              print("User disconnected!")
              print("Disconnecting WMI...")
              os.system("main.py")
          if msg == "rst -bt":
              print("Rebooting from: ",addr)
              print("Loading to be reboot...")
              os.system("main.py")
          if msg == "patch":
              print("Pacthing mode turned on!")
              print("Waiting client to insert patch location")
              if msg == "A:/" or "a:/" or "a":
                  print("Patching...")
                  for i in msg:
                      print(f"Patched on: {addr}")
                  print("Done patching!")
    conn.close()

def start():
    server.listen()
    print(f"On the client fastboot please enter the ip addres: {SERVER}")
    print(f"PORT: {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[FSTBT/ACTIVE CONNECTION] {threading.activeCount() - 1}")

print("[FSTBT]: Starting...")
start()
