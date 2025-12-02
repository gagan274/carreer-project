import json
import os 
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




def send_email(receiver_email, Subject, Message):
    message = 'Failed to send'
    try:
        sender_email = "sumanthgl2000@gmail.com"
        sender_password = "ibdj alem atfr lvei"
        # Create a secure connection with Zoho Mail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to the sender's email account
        server.login(sender_email, sender_password)

        # Create a MIMEMultipart message object
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(receiver_email)
        msg['Subject'] = Subject

        body = Message
        # Attach the message body with HTML MIME type
        msg.attach(MIMEText(body, 'html'))
        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        message = "Email sent successfully!"
        return message
    except (smtplib.SMTPException, smtplib.SMTPAuthenticationError) as e:
        print(f"Error sending email: {e}")
    finally:
        # Always close the connection
        server.quit()
        return message




        
 


 

