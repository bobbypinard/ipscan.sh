import subprocess

# ping -c 1 $x.$y | grep "64 bytes" | cut -d " " -f 4 | tr -d ':' &

command = 'ifconfig | grep "inet " | grep -v 127.0.0.1 | cut -d"." -f1-3 | tr -d "inet"|tr -d " "'
ping = subprocess.Popen(('ping', '-c', '1', '192.168.0.130'), stdout=subprocess.PIPE)

subprocess.run(command, shell=True)

for x in range(255):
    subprocess.run(('grep', '"64 bytes"'), stdin=ping.stdout)