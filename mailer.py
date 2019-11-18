import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv

class Email_Sender:
    def __init__(self, target_dir, id_email_path):
        self.target_dir = target_dir
        self.id_email_path = id_email_path

        self.email = "ajayraj.cseanits@gmail.com"
        self.password = ""

        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.email, self.password)

    def send_email(self, to_email_id, certificate_path):
        mail = MIMEMultipart()
        mail['From'] = self.email
        mail['To'] = to_email_id
        mail['Subject'] = "Participation Certificate for Ethical Hacking & Cybersecurity Workshop by Spyry at ANITS"

        message = ("Dear Student,",
                "We appreciate your participation in the Ethical Hacking & Cybersecurity Workhop by Spyry at ANITS.",
                "Please find your participation certificate attached with this email.",
                "For any discrepencies please email cursors2k19@anits.edu.in",
                "Regards,",
                "Cursors2k18 Team.")
        body = "\n\n".join(message)

        mail.attach(MIMEText(body, 'plain'))

        attachment_name = certificate_path.split('/')[-1]
        attachment = open(certificate_path, "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_name)

        mail.attach(part)
        text = mail.as_string()

        self.server.sendmail(self.email, to_email_id, text)

    def read_id_email(self):
        id_email_file = open(self.id_email_path, "r")
        self.id_email = list(csv.reader(id_email_file))
        id_email_file.close()

    def send_all_emails(self):
        for id, email in self.id_email:
            certificate_path = self.target_dir + "/" + id + ".pdf"
            if "@anits.edu.in" in email:#"@" in email and email.index("@") != len(email) - 1:
                email_id = email[:]
            else:
                email_id = email + "@gmail.com"

            try:
                self.send_email(email_id, certificate_path)
                print("Email successfully sent to", email)
            except:
                print("Email to", email_id, "failed")

    def __del__(self):
        self.server.quit()


'''
SAMPLE CALL
emailer = Email_Sender("/Users/ajayraj/Documents/CSI/CertificateGenerator/Target", "/Users/ajayraj/Documents/CSI/CertificateGenerator/sample.csv")
emailer.read_id_email()
emailer.send_all_emails()
'''