import socket
import time
import json

GATEWAY_IN = "192.168.1.1"      # This device acting as gateway, incoming leg
GATEWAY_OUT = "192.168.168.18"  # This device acting as gateway, outgoing leg
CAMERA = "192.168.1.2"          # The camera
SERVER = "192.168.168.20"      # The cloud based server instance

PORT_SRV = 3001                 # TCP port on server
PORT_CAM = 3000                 # TCP port on camera


s_in = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_in.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 'enxc0742bff7c63\0'.encode('utf-8'))
s_in.bind((GATEWAY_IN, PORT_CAM))

s_out = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_out.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, 'eth0\0'.encode('utf-8'))
s_out.bind((GATEWAY_OUT, 0))
connected = False
while not connected:
    try:
        s_out.connect((SERVER, PORT_SRV))
        connected = True
        print("Connected to server")
    except:
        print("Server connection failed")
        time.sleep(5)
        pass

while True:
    s_in.listen()
    conn_in, addr_in = s_in.accept()
    with conn_in:
        print("Connected to {}", addr_in)
        while True:
            data = conn_in.recv(2048)
            if not data:
                break
            print("Received: {}", data)
            jstring = json.loads(data.decode("utf-8")) 
            short_json = {"plateText":jstring["plateText"],
              "brand":jstring["vehicle_info"]["brand"],
              "model":jstring["vehicle_info"]["model"],
              "type":jstring["vehicle_info"]["type"],
              "color":jstring["vehicle_info"]["color"]
              }
            sdata = json.dumps(short_json)
            s_out.sendall(bytes(sdata, encoding="utf-8"))

