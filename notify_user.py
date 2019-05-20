import os
import smtplib

NETWORK_NAME = '238 Galoway Road'
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_DEFAULT_SENDER = os.environ.get('EMAIL_DEFAULT_SENDER')

with open('unknown-hosts.log', 'r') as f:
    log = f.read()


def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = f'UNKOWN HOSTS IN NETWORK {NETWORK_NAME}'
        print(subject)
        body = log
        msg = f'{subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)


if __name__ == '__main__':
    notify_user()
