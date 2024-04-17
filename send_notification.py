import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_gmail_notification(message):
    print("Sending notification now...")
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls() # encrypt the communication
        smtp.ehlo() # Identifies the mail server
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
        print(f"Notification sent successfully to {EMAIL_ADDRESS}")