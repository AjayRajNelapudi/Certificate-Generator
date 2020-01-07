from tkinter import *
from tkinter import messagebox
import certificates
import clicks
import mailer

points = None

def set_points():
    template = certificate_entry.get()
    points_capture = clicks.MouseClickCapture(template)
    points_capture.capture()
    global points
    points = points_capture.points

def generate_certificates():
    template = certificate_entry.get()
    participants = participants_entry.get()
    target_dir = target_dir_entry.get()

    try:
        global points
        gen = certificates.Certificate_Generator(template, participants)
        gen.set_data_positions(points)
        gen.make_certificates()
        gen.save_all(target_dir)
    except:
        messagebox.showerror('Status', 'Certificate Generation Failed')

    messagebox.showinfo('Status', 'Please check ' + target_dir)

def email_certificates():
    target_dir = target_dir_entry.get()
    mailing_list = mailing_list_entry.get()

    emailer = mailer.Mailer(target_dir, mailing_list)
    emailer.read_id_email()
    emailer.send_all_emails()

    messagebox.showinfo('Status', 'Certificates emailed. Please check your sent mailbox')

def open_filedialog(filepath):
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()
    filepath.set(askopenfilename())

def open_dirdialog(filepath):
    from tkinter import Tk
    from tkinter.filedialog import askdirectory

    Tk().withdraw()
    filepath.set(askdirectory())

window = Tk()
window.title('Cursors Certificate Generator')
window.geometry('700x500')

certificate_label = Label(window, text = 'Template')
certificate_label.place(x = 50, y = 50, width = 100, height = 50)

certificate_entry_var = StringVar()
certificate_entry = Entry(window, textvar = certificate_entry_var)
certificate_entry.place(x = 200, y = 50, width = 300, height = 50)

certificate_filedialog = Button(window, text = 'Select', command = lambda :open_filedialog(certificate_entry_var))
certificate_filedialog.place(x = 550, y = 50, width = 100, height = 50)

participants_label = Label(window, text = 'Participants')
participants_label.place(x = 50, y = 120, width = 100, height = 50)

participants_entry_var = StringVar()
participants_entry = Entry(window, textvar = participants_entry_var)
participants_entry.place(x = 200, y = 120, width = 300, height = 50)

participants_filedialog = Button(window, text = 'Select', command = lambda :open_filedialog(participants_entry_var))
participants_filedialog.place(x = 550, y = 120, width = 100, height = 50)

target_dir_label = Label(window, text = 'Target Dir')
target_dir_label.place(x = 50, y = 190, width = 100, height = 50)

target_dir_entry_var = StringVar()
target_dir_entry = Entry(window, textvar = target_dir_entry_var)
target_dir_entry.place(x = 200, y = 190, width = 300, height = 50)

target_dir_filedialog = Button(window, text = 'Select', command = lambda :open_dirdialog(target_dir_entry_var))
target_dir_filedialog.place(x = 550, y = 190, width = 100, height = 50)

mailing_list_label = Label(window, text = 'Mailing List')
mailing_list_label.place(x = 50, y = 260, width = 100, height = 50)

mailing_list_entry_var = StringVar()
mailing_list_entry = Entry(window, textvar = mailing_list_entry_var)
mailing_list_entry.place(x = 200, y = 260, width = 300, height = 50)

mailing_list_filedialog = Button(window, text = 'Select', command = lambda :open_filedialog(mailing_list_entry_var))
mailing_list_filedialog.place(x = 550, y = 260, width = 100, height = 50)

set_points_button = Button(window, text = 'Set Points', command = set_points)
set_points_button.place(x = 250, y = 320, width = 200, height = 50)

generate_button = Button(window, text = 'Generate Certificates', command = generate_certificates)
generate_button.place(x = 250, y = 360, width = 200, height = 50)

email_certificates_button = Button(window, text = 'Email Certificates', command = email_certificates)
email_certificates_button.place(x = 250, y = 400, width = 200, height = 50)

masthead = Label(window, text = 'Designed & Developed by Ajay Raj Nelapudi')
masthead.place(x = 200, y = 450, width = 300, height = 50)

window.mainloop()