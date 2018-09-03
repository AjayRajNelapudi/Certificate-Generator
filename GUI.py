from tkinter import *
import generator

def generate_certificates():
    certificate = certificate_entry.get()
    participants = participants_entry.get()
    generator.generate_certificates(certificate, participants)

    status = Label(window, text = 'Check your directory')
    status.pack()


window = Tk()
window.title('CSI Certificate Generator')
window.geometry('200x200')
window.resizable(width = False, height = False)

certificate_label = Label(window, text = 'Enter Certificate Template')
certificate_label.pack()

certificate_entry = Entry(window)
certificate_entry.pack()

participants_label = Label(window, text = 'Enter Participants File')
participants_label.pack()

participants_entry  = Entry(window)
participants_entry.pack()

generate_button = Button(window, text = 'Make Certificates', command = generate_certificates)
generate_button.pack()

window.mainloop()