import os
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formatdate, make_msgid
from email.mime.base import MIMEBase
from email import encoders

# Replace these with your email details
sender_email = "xyz@email.com" # replace with your phishing mail
subject = "Dhamaka Holiday Package Offer!!!"

# Path to the image in the Downloads directory
image_path = os.path.join(os.path.expanduser("~"), "Downloads", "SUMMER IN THAILAND.jpg")

# Path to the recipients file
recipients_file = "recipients.txt"

# Email content
text = """\
SPECIAL OFFER ONLY FOR EMPLOYEES
*SCAN THE CODE AND REGISTER BEFORE 15 JULY*
[image: SUMMER IN THAILAND.jpg]
*LIMITED OFFER*
***Conditions Apply
"""

html = """\
<div dir="ltr">
  <div style="text-align:center"><font size="1">SPECIAL OFFER ONLY FOR EMPLOYEES</font></div>
  <div style="text-align:center"><b><font color="#ff0000">SCAN THE CODE AND REGISTER BEFORE 15 JULY</font></b></div>
  <div style="text-align:center"><img src="cid:ii_lyfic45y0" alt="SUMMER IN THAILAND.jpg" width="472" height="472"><br></div>
  <div style="text-align:center"><b><font color="#ff0000">LIMITED OFFER</font></b><br><font size="1">***Conditions Apply</font></div>
</div>
"""

# Read recipient emails from the file
def read_recipients(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file if line.strip()]

# Create the email message
def create_message(sender_email, receiver_email, subject, text, html):
    msg = MIMEMultipart("related")
    msg["MIME-Version"] = "1.0"
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid()
    msg["Subject"] = subject
    msg["From"] = "Dhamaka Offer <xyz@email.com>" #replace with your phishing email address
    msg["To"] = receiver_email

    # Create the alternative part
    alt_part = MIMEMultipart("alternative")
    msg.attach(alt_part)

    # Attach the plain text part
    alt_part.attach(MIMEText(text, "plain"))

    # Attach the HTML part
    alt_part.attach(MIMEText(html, "html"))

    # Attach the image
    with open(image_path, "rb") as img_file:
        img = MIMEImage(img_file.read())
        img.add_header("Content-ID", "<ii_lyfic45y0>")
        img.add_header("Content-Disposition", "attachment", filename="SUMMER IN THAILAND.jpg")
        msg.attach(img)
    
    return msg

# SMTP server configuration for local server
smtp_server = "10.10.10.10" # replace with your smtp server ip 
port = 25  # replace with your port for SMTP servers

try:
    # Connect to the local SMTP server
    with smtplib.SMTP(smtp_server, port) as server:
        # No need for authentication for a local server
        
        # Read recipients from file
        receiver_emails = read_recipients(recipients_file)
        
        for receiver_email in receiver_emails:
            msg = create_message(sender_email, receiver_email, subject, text, html)
            # Send email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Email sent successfully to {receiver_email}!")
except Exception as e:
    print(f"Error sending email: {e}")
