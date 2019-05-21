# Network Monitor
Python script to monitor your network for unknown hosts. An email alert will be sent to the specified user when an unknown host is detected on the network with information about the unknown device.

## Utilizes
* Cron
* Nmap
* Bash Scripting
* Python SMTP Library
* Logging

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Requirements
* nmap
* Python3.6+
* pip3
* Google App Password: https://myaccount.google.com/apppasswords

### Installation

Setup configuration file for email services and your linode token.
```
sudo nano ~/.bash_config
```
```
{
        "MAIL_USERNAME":"email",
        "GOOGLE_APP_PASS":"google app password",
}
```
Clone the repository onto your machine.
```
git clone https://github.com/itzliu/network-monitor.git
```
Change directory into the project directory folder.
```
cd network-monitor
```
Create a file for known devices on your network. You can use the arp command to see the devices currently on your network.
```
sudo nano known-hosts
```
```
[device address 1]
[device address 2]
[device address 3...]
```
Create a virtual environment for the app.
```
python3.6 -m venv venv
```
Activate your virtual environment.
```
source venv/bin/activate
```
Run script.
```
python monitor.py
```

To automate this script to check your websites you can do the following.

Find Python environment path. (something like '~/network-monitor/venv/bin/python')
```
which python
```
Open cron
```
crontab -e
```
Add this to the cron script to run the monitor script every 10 minutes.
```
*/10 * * * * . $HOME/.bash_config && [environement path] [monotor.py path]
```

## Authors
* Harry Liu
