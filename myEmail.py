import imghdr
import smtplib
import os
from email.message import EmailMessage

email_id = 'thaksha2011@gmail.com'
email_pass = "hklftjangbkmkxod"

contacts = ['jathuseelan96@gmail.com', 'jathuseelan59@gmail.com']

msg = EmailMessage()
msg['Subject'] = 'Mail for Jathu'
msg['From'] = 'thaksha2011@gmail.com'
msg['To'] = ','.join(contacts)
msg.set_content('Hey, I am Jathu')

current_directory = os.getcwd()  # Get the current working directory
pdf_file_path = os.path.join(current_directory, 'DE.pdf')
files = [pdf_file_path]

for file in files:
    with open(file, 'rb') as m:
        file_data = m.read()
        file_type = imghdr.what(m.name)
        file_name = m.name

msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id, email_pass)
    smtp.send_message(msg)


# import smtplib
# import os
#
# email_id = 'thaksha2011@gmail.com'
#     # os.environ.get('EMAIL_ADDR')
# email_pass = "hklftjangbkmkxod"
#     # os.environ.get('EMAIL_PASS')
#
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#
#     smtp.login(email_id, email_pass)
#
