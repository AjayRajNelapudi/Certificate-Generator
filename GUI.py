from tkinter import *
from tkinter import messagebox
import certificates
import placetext

points = None

def set_points():
    template = certificate_entry.get()
    points_capture = placetext.Mouse_Click_Capture(template)
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
        gen.extract_contestants_data(points)
        gen.make_certificates()
        gen.save_all(target_dir)
    except:
        pass
        #open a dialog box and display the error message here

    messagebox.showinfo('Status', 'Please check ' + target_dir)

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
window.title('CSI Certificate Generator')
window.geometry('700x400')

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
participants_entry  = Entry(window, textvar = participants_entry_var)
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

set_points_button = Button(window, text = 'Set Points', command = set_points)
set_points_button.place(x = 250, y = 260, width = 200, height = 50)

generate_button = Button(window, text = 'Generate Certificates', command = generate_certificates)
generate_button.place(x = 250, y = 340, width = 200, height = 50)

window.mainloop()