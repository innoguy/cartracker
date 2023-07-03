This repository contains a number of python scripts for the Cirrus car tracking project

The physical setup used contains 3 components:
- a RPI2 emulating an AXIS camera with CAMMRA app sending events over ethernet port eth0 with static IP address 192.168.1.2/24 connected per ethernet cable to the input ethernet port of an OrangePi R1
- an OrangePi R1 with 
    - ethernet port enxc0742bff7c63 configured with static IP address 192.168.1.1/24 
    - ethernet port eth0 configured with DHCP connected to local network and IP 192.168.168.18
- a Macbook connected to that same local network over ethernet with DHCP IP 192.168.168.20

The RPI2
- runs camera.py script as systemd service
- sends out a simulated json event for a fictitious passing car to the OrangePi R1

The OragePi R1
- runs gateway.py script as systemd service
- receives the long json event from RPI2, filters it out and sends shortened json to Macbook server

The Macbook
- runs server.py script 
- displays the received shortened json on screen