# http://naelshiab.com/tutorial-send-email-python/

import smtplib
from email.mime import multipart
from email.mime import text

fromaddr = 'bot@davidjaggi.com'
toaddr = 'm.merz@hss17.qmul.ac.uk'
msg = multipart.MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Test E-Mail!'

body = 'This is a test email!'
msg.attach(text.MIMEText(body,'plain'))

server = smtplib.SMTP()
server.connect('login-178.hoststar.ch')
server.login(fromaddr, 'Password')
server.starttls()

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
