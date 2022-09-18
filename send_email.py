import os
import smtplib
from email.message import EmailMessage
import imghdr

email = os.environ.get('dummy_email')
pass_email = os.environ.get('dummy_email_pass')

msg = EmailMessage()
msg['Subject'] = 'Random Cute Kitties'
msg['From'] = email
msg['To'] = email
msg.set_content('Image attached to the mail...')

files = ["Desktop/Projects/Send_Email/Cat1.jpg", "Desktop/Projects/Send_Email/Cat2.jpg"]

# HTML Section

msg.add_alternative("""\
    <!DOCTYPE HTML>
    <html>
        <body>
            <h1 style='color:SlateGrey;'> Here are the two images you requested. </h1>
            <p> The two kittens in the images were obtained from random websites online. </p>
        </body>
    </html>
    """, subtype = 'html')

for file in files:  
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename = file_name)
    #msg.add_attachment(file_data, maintype = 'application', subtype = 'octet-stream', filename = file_name) -- For pdfs and other file data

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email, pass_email)

    smtp.send_message(msg)
 
'''
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email, pass_email)

    subject = 'Regarding the interview scheduled'
    body = 'We have set the date for 10-10-2020'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(email, email, msg)
'''
