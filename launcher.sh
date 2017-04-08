#!/bin/bash
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

vncserver
cd /
cd /home/pi/RPIC
git pull
sudo python button.py &
cd /
