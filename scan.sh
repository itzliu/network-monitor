#!/bin/bash

# Detect hosts.
nmap -sP 192.168.1.0/24 | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > /home/pi/router-monitor/detected-hosts

# Compare detected hosts and known hosts.
grep -Fxv -f /home/pi/router-monitor/known-hosts /home/pi/router-monitor/detected-hosts > /home/pi/router-monitor/unknown-hosts

# Scan unknown hosts.
if  [ -s /home/pi/router-monitor/unknown-hosts ]
then
	nmap -O -iL /home/pi/router-monitor/unknown-hosts > /home/pi/router-monitor/unknown-hosts-scan
	cat /home/pi/router-monitor/unknown-hosts-scan >> /home/pi/logs/unknown-hosts.log
fi
