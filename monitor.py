import os
import subprocess
import smtplib

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
NETWORK_NAME = 'HOME ROUTER'
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('GOOGLE_APP_PASS')
EMAIL_DEFAULT_SENDER = os.environ.get('EMAIL_DEFAULT_SENDER')

def notify_user():

    file = f'{DIR_PATH}/unknown-hosts-scan'

    with open(f'{file}', 'r') as f:
        log = f.read()

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = f'UNKOWN HOSTS IN NETWORK {NETWORK_NAME}'
        body = log
        msg = f'{subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)

def scan():
    command = f'{DIR_PATH}/scan.sh'
    p = subprocess.Popen(['sudo',command])
    p.wait()
    if os.stat(f"{DIR_PATH}/unknown-hosts").st_size == 0:
        return False
    return True

if __name__ == '__main__':
    if scan():
    	notify_user()
