#!/bin/bash

cd /home/pi/.homeassistant
git pull
sudo systemctl restart home-assistant