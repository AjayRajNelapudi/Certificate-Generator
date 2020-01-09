from certificates import CertificateGenerator
from clicks import MouseClickCapture
from mailer import Mailer
from view import View
from tkinter import messagebox
import logging
import logging.config
import os
import webbrowser
import traceback

class Controller:
    points = None
    logger = None
    certificates_generated = False
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "default": {
                "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
            },
        },
        "handlers": {
            "main": {
                "class": "logging.FileHandler",
                "formatter": "default",
                "filename": "logs/main.log"
            },
            "controller": {
                "class": "logging.FileHandler",
                "formatter": "default",
                "filename": "logs/controller.log"
            },
            "certificates": {
                "class": "logging.FileHandler",
                "formatter": "default",
                "filename": "logs/certificates.log"
            },
            "mailer": {
                "class": "logging.FileHandler",
                "formatter": "default",
                "filename": "logs/mailer.log"
            },
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "stream": "ext://sys.stdout"
            }
        },
        "loggers": {
            "controller": {
                "handlers": ["controller", "main"],
                "level": "INFO",
            },
            "certificates": {
                "handlers": ["certificates", "main"],
                "level": "INFO",
            },
            "mailer": {
                "handlers": ["mailer", "main"],
                "level": "INFO",
            },
        }
    }

    @staticmethod
    def config():
        if "logs" not in os.listdir(os.getcwd()):
            os.mkdir("logs")
        logging.config.dictConfig(Controller.LOGGING)
        Controller.logger = logging.getLogger("controller")

        View.window.protocol('WM_DELETE_WINDOW', Controller.quit)
        View.certificate_filedialog['command'] = lambda: Controller.open_filedialog(View.certificate_entry_var)
        View.participants_filedialog['command'] = lambda: Controller.open_filedialog(View.participants_entry_var)
        View.target_dir_filedialog['command'] = lambda: Controller.open_dirdialog(View.target_dir_entry_var)
        View.mailing_list_filedialog['command'] = lambda: Controller.open_filedialog(View.mailing_list_entry_var)
        View.set_points_button['command'] = Controller.set_points
        View.generate_button['command'] = Controller.generate_certificates
        View.email_certificates_button['command'] = Controller.email_certificates
        View.masthead.bind("<Button-1>", lambda e: webbrowser.open("https://ajayrajnelapudi.github.io/"))
        View.profile_redirect['command'] = lambda: webbrowser.open("https://ajayrajnelapudi.github.io/")

    @staticmethod
    def set_points():
        template = View.certificate_entry.get()
        if template == None or template == '':
            messagebox.showwarning(
                "Operational Error",
                "Please select the template before setting points."
            )
            Controller.logger.info('Empty template')
            return

        points_capture = MouseClickCapture(template)
        points_capture.display_template()
        Controller.points = points_capture.points

        Controller.certificates_generated = False
        Controller.logger.info("Points Captured. " + str(Controller.points))

    @staticmethod
    def generate_certificates():
        if Controller.points == None or Controller.points == []:
            messagebox.showwarning(
                "Operational Error",
                "Please set points before generating certificates."
            )
            Controller.logger.info("generate_certificates() called before set_points()")
            return

        template = View.certificate_entry.get()
        participants = View.participants_entry.get()
        target_dir = View.target_dir_entry.get()

        try:
            generator = CertificateGenerator(template, participants)
            generator.set_data_positions(Controller.points)
            generator.make_certificates()
            generator.save_all(target_dir)

            Controller.certificates_generated = True
            messagebox.showinfo("Certificates Generated", "Please check " + target_dir)
            Controller.logger.info("all certificates generated successfully")
        except Exception as exp:
            exception = ''.join(traceback.format_exception(etype=type(exp), value=exp, tb=exp.__traceback__))
            Controller.logger.info("generator failed due to the following reason")
            Controller.logger.info(exception)
            messagebox.showerror("Unknown exception in generator", exception)

    @staticmethod
    def email_certificates():
        if not Controller.certificates_generated:
            messagebox.showerror(
                "Operational Error",
                "Certificates not generated yet."
            )
            Controller.logger.info("email_certificates() called before generate_certificates()")
            return

        target_dir = View.target_dir_entry.get()
        mailing_list = View.mailing_list_entry.get()

        try:
            mailer = Mailer(target_dir, mailing_list)
            mailer.read_id_email()
            mailer.send_all_emails()

            messagebox.showinfo(
                "Mailer Info",
                "Emails dispatched successfully. Check your sent box."
            )
            Controller.logger.info("Emails dispatched successfully")
        except Exception as exp:
            exception = ''.join(traceback.format_exception(etype=type(exp), value=exp, tb=exp.__traceback__))
            Controller.logger.info("mailer failed due to the following reason")
            Controller.logger.info(exception)
            messagebox.showerror("Unknown exception in mailer", exception)

    @staticmethod
    def open_filedialog(filepath):
        from tkinter import Tk
        from tkinter.filedialog import askopenfilename

        Tk().withdraw()
        filepath.set(askopenfilename())

    @staticmethod
    def open_dirdialog(filepath):
        from tkinter import Tk
        from tkinter.filedialog import askdirectory

        Tk().withdraw()
        filepath.set(askdirectory())

    @staticmethod
    def quit():
        View.window.destroy()

if __name__ == "__main__":
    Controller.config()
    View.render()