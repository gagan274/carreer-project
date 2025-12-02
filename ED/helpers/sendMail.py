import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(receiver_email, Subject, Message):
    message = 'Failed to send'
    print(receiver_email)
    print(Subject)
    print(Message)
    try:
        sender_email = "vishwas.c@gndsolutions.in"
        sender_password = "iM6pTvn4PjGz"
        # Create a secure connection with Zoho Mail's SMTP server
        server = smtplib.SMTP('smtp.zoho.com', 587)
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
        

# # Example usage
#   # Replace with actual app password
# receiver_email = ["anil.reddy@gndsolutions.in"]
# subject = "Hi this is to test"
# body = """
# <p>Dear recipient,</p>
# <p>This is a test email.</p>

# <p>Best regards,<br>
# <p><img src="cid:image1" style="max-width:100%; height: auto;"></p>
# """

# # Path to the image you want to attach
# image_path = "1.png"

# send_email(receiver_email, subject, body)
