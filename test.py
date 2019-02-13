import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "ajayraj.cseanits@gmail.com"
toaddr = "najayraj.16.cse@anits.edu.in"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Spyry Workshop E-Certificate"

body = "TEXT YOU WANT TO SEND"

msg.attach(MIMEText(body, 'plain'))

filename = "68.pdf"
attachment = open("/Users/ajayraj/Documents/CSI/CertificateGenerator/Target/68.pdf", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "anitscse034")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
