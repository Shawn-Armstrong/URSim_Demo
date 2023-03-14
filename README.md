# README.md

## Overview
- I start a URSim then connect with it using a Python client over the network via TCP/IP sockets.
- I send the command `movej([0, 0, 0, 0, 0, 0], a=1.0, v=1.0)\n` and it executes. 
- URSim controller responds with binary data in hexadecimal format in an unknown encoding:

  ```Console
  \x00\x00\x007\x14\xff\xff\xff\xff\xff\xff\xff\xff\xfe\x03\tURControl\x05\r\x00\x00\x00\x00\x00\x00\x00\x0013-10-2022, 09:22:44\x00\x00\x00\x18\x14\xff\xff\xff\xff\xff\xff\xff\xff\xfe\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x01
  ```

## Instructions
1. Run the following commands:
     
   ```Console
   git clone https://github.com/Shawn-Armstrong/URSim_Demo.git
   cd URSim_Demo
   ./start_sim.sh
   ```
2. Go to [http://localhost:6080/vnc_auto.html](http://localhost:6080/vnc_auto.html) and start the cobot.
3. Inside directory `URSim_Demo` run the following command:
     
   ```Console
   python3 client.py
   ```
