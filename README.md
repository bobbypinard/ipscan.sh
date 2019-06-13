# ipscan script

The script can detect and will show all reachable ip addresses from a specified range.
 
 Run the script followed by the first 3 octets of the network you want to scan.
 ```
 ./ipscan.sh 192.168.1 
 ```
 
 By default the script runs through address 1 - 254 in the last octet. 
 
 The range that is looped through can be changed. Simply change the seq numbers.
 ```
 for ipaddress in `seq 1 254`; do
 ```
 


