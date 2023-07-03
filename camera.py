#!/usr/bin/python3

import socket
import json
import time
import string
import random
from datetime import datetime

cars = json.load(open('carsample.json')) 
total = len(cars)

HOST = "192.168.1.1"  # The server's hostname or IP address
PORT = 3000  # The port used by the server

PACKET = {"packetCounter":"7595700",
"capture_timestamp":"1638961134132",
"frame_timestamp":"1638961134132653",
"capture_ts":"1638961134132000000",
"datetime":"20211208 125854132",
"plateText":"\u0043\u0041\u0032\u0032\u0032\u0038\u0041\u004d",
"plateUnicode":"\u0043\u0041\u0032\u0032\u0032\u0038\u0041\u004d",
"plateUTF8":"CA2228AM",
"plateASCII":"CA2228AM",
"plateCountry":"UKR",
"plateConfidence":"0.708942",
"carState":"new",
"roiID":"1",
"geotag":{"lat": 50.418114,"lon": 30.476213},"imageType": "frame","plateImageType": "jpeg","plateImageSize": "0","carMoveDirection":"unknown",
"timeProcessing":"0",
"plateCoordinates":[1193, 439, 98, 20],
"plateCoordinatesRelative":[1176, 439, 98, 20],
"carID":"521893",
"GEOtarget":"Camera",
"imagesURI":["/local/fflprapp/tools.cgi?action=getImage&name=24/20211208105854_132_lp_CA2228AM_UKR_Opel_Astra G_SILVER.jpg","/local/fflprapp/tools.cgi?action=getImage&name=25/20211208105854_132_roi_CA2228AM_UKR_Opel_Astra G_SILVER.jpg"],
"imageFile":"/var/spool/storage/SD_DISK/fflprapp/images/25/20211208105854_132_roi_CA2228AM_UKR_Opel_Astra G_SILVER.jpg",
"vehicle_info":{"brand":"Opel","model":"Astra G","type":"CAR","color":"SILVER","confidenceMMR":"96.657967","confidenceColor":"97.237495","coordinates":[1012, 272, 458, 272]},
"camera_info":{"SerialNumber":"ACCC8EA617EF","ProdShortName":"AXIS P1445-LE","MACAddress":"AC:CC:8E:A6:17:EF"},
"sensorProviderID":"defaultID_175"
}

template = json.dumps(PACKET)
plate_character = string.ascii_uppercase + '0123456789'

state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

colors = ["red", "white", "blue", "green", "yellow", "grey", "black"]

def random_plate():
    p = ''
    for i in range(7):
        p += random.choice(plate_character)
    return p


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    connected = False
    while not connected:
        try:
            s.connect((HOST, PORT))
            connected = True
        except Exception as e:
            pass

    while True:
        index = random.randrange(total)
        car = cars[index]
        PACKET["capture_timestamp"]=str(int(time.time()))
        PACKET["plateUTF8"]=random_plate()
        PACKET["plateCountry"]=random.choice(state_names)
        PACKET["vehicle_info"]["brand"]=car["Make"]
        PACKET["vehicle_info"]["model"]=car["Model"]
        PACKET["vehicle_info"]["type"]=car["Category"]
        PACKET["vehicle_info"]["color"]=random.choice(colors)
        data = json.dumps(PACKET)
        s.sendall(bytes(data, encoding="utf-8"))
        print(data)
        time.sleep(10)


