#!/bin/bash

apt-get update
apt-get install -y unzip

cd /workspace

# Download and unzip the OpenCompass data
wget https://github.com/open-compass/opencompass/releases/download/0.2.2.rc1/OpenCompassData-complete-20240207.zip
unzip OpenCompassData-complete-20240207.zip
cd ./data
find . -name "*.zip" -exec unzip "{}" \;

cd /workspace
rm -rf OpenCompassData-complete-20240207.zip