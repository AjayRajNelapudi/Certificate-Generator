import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv
import os
import traceback

class Mailer:
    def __init__(self, target_dir, id_email_path):
        self.target_dir = target_dir
        self.id_email_path = id_email_path

        '''
        If you have want to add your email to dispatch certificates, change the below code
        and turn on access to less secure apps at
        https://myaccount.google.com/lesssecureapps?pli=1
        '''
        self.login_email = "certificates34@gmail.com"
        self.login_password = ""

        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()

        if self.login_password == "":
            raise ValueError("Password might have been removed for security concerns. Please add password")

        self.server.login(self.login_email, self.login_password)

        self.logger = logging.getLogger("mailer")

    def build_and_send(self, to_email_id, certificate_path):
        mail = MIMEMultipart()
        mail['From'] = self.login_email
        mail['To'] = to_email_id

        # Change subject of email here
        mail['Subject'] = "Participation Certificate for ACM Hour of Code"

        # Change body of email here
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

        self.server.sendmail(self.login_email, to_email_id, text)

    def read_id_email(self):
        with open(self.id_email_path, "r") as id_email_file:
            self.id_email = list(csv.reader(id_email_file))

    def send_all_emails(self):
        for id, email in self.id_email:
            certificate_path = os.path.join(self.target_dir, id + ".pdf")
            try:
                self.build_and_send(email, certificate_path)
                self.logger.info("Email sent to " + email)
            except Exception as exp:
                exception = ''.join(traceback.format_exception(etype=type(exp), value=exp, tb=exp.__traceback__))
                self.logger.info("Email to " + email + "failed due to the following exception")
                self.logger.info(exception)

    def __del__(self):
        self.server.quit()