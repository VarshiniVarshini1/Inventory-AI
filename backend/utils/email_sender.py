import smtplib
from email.message import EmailMessage
import config

def send_email(to, subject, content):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = config.EMAIL_USER
    msg["To"] = to
    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(config.EMAIL_USER, config.EMAIL_PASS)
        smtp.send_message(msg)

    return "Email sent"
