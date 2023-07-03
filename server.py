import socket
import json

HOST = '192.168.168.20'                  
PORT = 3001                 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen()
conn, addr = s.accept()
with conn:
    print("Connected to {}", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        jstring = json.loads(data.decode("utf-8"))
        print("Received: ", jstring)

