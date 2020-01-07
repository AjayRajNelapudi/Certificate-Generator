import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import os

class Mailer:
    def __init__(self, target_dir, id_email_path):
        self.target_dir = target_dir
        self.id_email_path = id_email_path

        self.email = "certificates34@gmail.com"
        self.password = "anitscse@noreply"

        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        # self.server.ehlo()
        self.server.starttls()
        self.server.login(self.email, self.password)

    def build_and_send(self, to_email_id, certificate_path):
        mail = MIMEMultipart()
        mail['From'] = self.email
        mail['To'] = to_email_id
        mail['Subject'] = "Participation Certificate for ACM Hour of Code"

        message = [
            "Dear Student,",
            "We appreciate your participation in the ACM Hour of Code.",
            "Apologies for the delay. Please find your participation certificate attached with this email.",
            "For any discrepencies please let us know in the WhatsApp group",
            "Regards,",
            "ACM Student Chapter, ANITS."
        ]
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
        attachment.close()

        self.server.sendmail(self.email, to_email_id, text)

    def read_id_email(self):
        id_email_file = open(self.id_email_path, "r")
        self.id_email = list(csv.reader(id_email_file))
        id_email_file.close()

    def send_all_emails(self):
        for id, email in self.id_email:
            certificate_path = os.path.join(self.target_dir ,id + ".pdf")
            try:
                self.build_and_send(email, certificate_path)
                print("Email successfully sent to", email)
            except:
                print("Email to", email, "failed")

    def __del__(self):
        self.server.quit()