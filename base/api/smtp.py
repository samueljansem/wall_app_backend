import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import environ


# Initialise environment variables
env = environ.Env()
environ.Env.read_env()


def send_welcome_email(text='', subject='', to_emails=[]):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = env('SMTP_USER')
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    msg_str = msg.as_string()
    server = smtplib.SMTP(host=env('SMTP_HOST'), port=env('SMTP_PORT'))
    server.ehlo()
    server.starttls()
    server.login(env('SMTP_USER'), env('SMTP_PASSWORD'))
    server.sendmail(env('SMTP_USER'), to_emails, msg_str)
    server.quit()
