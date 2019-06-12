#!/bin/bash

echo "-example: ./ipscan.sh 192.168.1 "

for ipaddress in `seq 1 254`; do 
ping -c 1 $1.$ipaddress | grep "64 bytes" | cut -d " " -f 4 | tr -d ':' &
done
