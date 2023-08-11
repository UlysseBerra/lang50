import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_mail(subject, recipient, body):
    msg = MIMEMultipart()
    msg["From"] = os.getenv("email_address")
    msg["To"] = str(recipient)
    msg["Subject"] = str(subject)
    msg.attach(MIMEText(str(body), "plain"))
    
    server = smtplib.SMTP(os.getenv("email_server"), 587)
    server.starttls()
    
    server.login(os.getenv("email_address"), os.getenv("email_password"))
    text = msg.as_string()
    server.sendmail(os.getenv("email_address"), recipient, str(text))
    
    server.quit()
    