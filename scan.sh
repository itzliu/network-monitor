#!/bin/bash

# Detect hosts.
nmap -sP 192.168.1.0/24 | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > $HOME/network-monitor/detected-hosts

# Compare detected hosts and known hosts.
grep -Fxv -f $HOME/network-monitor/known-hosts $HOME/network-monitor/detected-hosts > $HOME/network-monitor/unknown-hosts

# Scan unknown hosts.
if  [ -s $HOME/network-monitor/unknown-hosts ]
then
	nmap -O -iL $HOME/network-monitor/unknown-hosts > $HOME/network-monitor/unknown-hosts-scan
	cat $HOME/network-monitor/unknown-hosts-scan >> $HOME/logs/unknown-hosts.log
fi
