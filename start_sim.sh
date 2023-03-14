#!/bin/bash

# Start simulator
docker network create --subnet=192.168.56.0/24 ursim_net
docker run -it -e ROBOT_MODEL=UR3e --net ursim_net --ip 192.168.56.101 -p 30002:30002 -p 30004:30004 -p 6080:6080 --name ur3e_container universalrobots/ursim_e-series



