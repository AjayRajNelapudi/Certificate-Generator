# Certificate-Generator
Software brought to life based on the necessity to create and email 300 certificates to students, for the Spyry Workshop held at ANITS college, as a part of Cursors 2k19.
Github repo: [https://github.com/AjayRajNelapudi/Certificate-Generator](https://github.com/AjayRajNelapudi/Certificate-Generator)

### Inputs:
1. Template: An image in .png, .jpg, or .jpeg format, containing the certificate template upon which names will be written.
2. Participants: A CSV file in which each row represents the data to be printed on each template.  
**Format**:<br>
field1,field2,field3,...,fieldN<br>
Such that field1 is always the name of the candidate.  
**Example**:<br>
Ajay Raj Nelapudi,IV/IV - CSE - A<br>
Shiv Shankar Singh,IV/IV - CSE - A

3. Target dir: The directory where all the certificates should be saved in.
4. Email Config: A JSON file in the following format.
```
{
    'credentials': {
        'login_email': 'youremailaddress@gmail.com',
        'login_password': 'yourpassword'
    },

    'mail': {
        'subject': 'Email subject',
        'body': 'Email body'
    }
}
```
5. Mailing List: A CSV file in which each row consists of the name and email address of each participant.
**Format**:<br>
name,email<br>
The name should match the name at field1 in participants.  
**Example**:<br>
Ajay Raj Nelapudi,ajayraj.cseanits@gmail.com<br>
Shiv Shankar Singh,shivshankarsingh@gmail.com<br><br>

### Outputs:
1. Certificates in .pdf format will be generated and saved at the dir given in target dir field.<br>
2. Emails will be sent to the the address given in the mailing list.<br><br>

### Instructions to change email:
1. When creating the email-config.json file, please add your credentials accordingly.
2. Login to the same email account in your browser and visit [https://myaccount.google.com/lesssecureapps?pli=1](https://myaccount.google.com/lesssecureapps?pli=1)
3. Turn on **Allow less secure apps** as shown below.
![Helper Image](https://content.screencast.com/users/ajayraj_anits/folders/Jing/media/3a863393-3b2d-4fed-b563-fc8c9c5c517a/00000402.png)

You should be able to send the certificates from your desired email account now.

For any problems during usage, please raise an issue at [Github issues](https://github.com/AjayRajNelapudi/Certificate-Generator/issues).


**To avoid any conflicts, please read the LICENSE and follow accordingly.**
