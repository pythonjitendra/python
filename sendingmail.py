# SENDING MAIL
# What is SMTP
# POP IMAP
# what is Portocol?

# First python mail source code
'''import smtplib
message = 'Subject: {}\n\n{}'.format("Test", "Hi ")
fromby="XXXXXXXXXXXXXXXXXXXXX"
to="XXXXXXXXXXXXXXXXXXXXXX"
# Init
mail=smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login("XXXXXXXXXXXXXXXXXXXXX","XXXXXXXXXXXXXXXXXXXXX")
mail.sendmail(fromby,to,message)
mail.quit()
print('Mail sent sucessfully')'''


# Mail Subject With Atatchement
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg['From'] = 'XXXXXXXXXXXXXXXXXXXXX'
msg['To'] = 'XXXXXXXXXXXXXXXXXXXXX'
msg['Subject'] = "test mail"
body = "Hi First test mail"

msg.attach(MIMEText(body, 'plain'))
filename = "test2.txt"
attachment = open("test2.txt", "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
message = 'Subject: {}\n\n{}'.format("Test", "Hi ")
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
text=msg.as_string()
s.login("XXXXXXXXXXXXXXXXXXXXX","XXXXXXXXXXXXXXXXXXXXX")
s.sendmail('XXXXXXXXXXXXXXXXXXXXX', 'XXXXXXXXXXXXXXXXXXXXX',text)
s.quit()
print('mail sent')
