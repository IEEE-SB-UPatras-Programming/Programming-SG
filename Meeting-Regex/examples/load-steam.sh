#!/bin/bash

f=$1

name=$(grep -oP '"name"\s+\K"(.+)' -m 1 $f | tr -d '"')
gameid=$(echo $f | grep -oP "\d+")

echo "Name:" $name 
echo "ID:" $gameid
