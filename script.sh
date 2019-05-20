# Detect hosts.
nmap -sP 192.168.1.0/24 | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > ~/router-monitor/detected-hosts

# Compare detected hosts and known hosts.
grep -Fxv -f ~/router-monitor/known-hosts ~/router-monitor/detected-hosts > ~/router-monitor/unknown-hosts

# nmap scan unknown hosts
nmap -O -iL ~/router-monitor/unknown-hosts >> ~/router-monitor/unknown-hosts.log

# Remove unnecessary files.
rm detected-hosts unknown-hosts
