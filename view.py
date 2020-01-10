from tkinter import *

class View:
    window = Tk()
    window.title('Certificate Generator')
    window.geometry('700x600')

    certificate_label = Label(window, text = 'Template')
    certificate_label.place(x = 50, y = 50, width = 100, height = 50)

    certificate_entry_var = StringVar()
    certificate_entry = Entry(window, textvar = certificate_entry_var)
    certificate_entry.place(x = 200, y = 50, width = 300, height = 50)

    certificate_filedialog = Button(window, text = 'Select')
    certificate_filedialog.place(x = 550, y = 50, width = 100, height = 50)

    participants_label = Label(window, text = 'Participants')
    participants_label.place(x = 50, y = 120, width = 100, height = 50)

    participants_entry_var = StringVar()
    participants_entry = Entry(window, textvar = participants_entry_var)
    participants_entry.place(x = 200, y = 120, width = 300, height = 50)

    participants_filedialog = Button(window, text = 'Select')
    participants_filedialog.place(x = 550, y = 120, width = 100, height = 50)

    target_dir_label = Label(window, text = 'Target Dir')
    target_dir_label.place(x = 50, y = 190, width = 100, height = 50)

    target_dir_entry_var = StringVar()
    target_dir_entry = Entry(window, textvar = target_dir_entry_var)
    target_dir_entry.place(x = 200, y = 190, width = 300, height = 50)

    target_dir_filedialog = Button(window, text = 'Select')
    target_dir_filedialog.place(x = 550, y = 190, width = 100, height = 50)

    email_config_label = Label(window, text = 'Email Config')
    email_config_label.place(x = 50, y = 260, width = 100, height = 50)

    email_config_entry_var = StringVar()
    email_config_entry = Entry(window, textvar = email_config_entry_var)
    email_config_entry.place(x = 200, y = 260, width = 300, height = 50)

    email_config_filedialog = Button(window, text = 'Select')
    email_config_filedialog.place(x = 550, y = 260, width = 100, height = 50)

    mailing_list_label = Label(window, text = 'Mailing List')
    mailing_list_label.place(x = 50, y = 330, width = 100, height = 50)

    mailing_list_entry_var = StringVar()
    mailing_list_entry = Entry(window, textvar = mailing_list_entry_var)
    mailing_list_entry.place(x = 200, y = 330, width = 300, height = 50)

    mailing_list_filedialog = Button(window, text = 'Select')
    mailing_list_filedialog.place(x = 550, y = 330, width = 100, height = 50)

    set_points_button = Button(window, text = 'Set Points')
    set_points_button.place(x = 250, y = 390, width = 200, height = 50)

    generate_button = Button(window, text = 'Generate Certificates')
    generate_button.place(x = 250, y = 430, width = 200, height = 50)

    email_certificates_button = Button(window, text = 'Email Certificates')
    email_certificates_button.place(x = 250, y = 470, width = 200, height = 50)

    masthead = Label(window, text = 'Designed & Developed by Ajay Raj Nelapudi')
    masthead.place(x = 200, y = 530, width = 300, height = 30)

    profile_redirect = Button(window, text = "Visit developer's profile")
    profile_redirect.place(x = 250, y = 560, width = 200, height = 25)

    @staticmethod
    def render():
        View.window.mainloop()