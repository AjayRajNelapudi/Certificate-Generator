# Certificate-Generator
Software brought to life based on the necessity to create and email 300 certificates to students, for the Spyry Workshop held at ANITS college, as a part of Cursors 2k19.

### Inputs:
1. Template: An image in .png, .jpg, or .jpeg format, containing the certificate template upon which names will be written.<br>
2. Participants: A CSV file in which each row represents the data to be printed on each template.  
**Format**:<br>
field1,field2,field3,...,fieldN<br>
Such that field1 is always the name of the candidate.  
**Example**:<br>
Ajay Raj Nelapudi,IV/IV - CSE - A<br>
Shiv Shankar Singh,IV/IV - CSE - A<br>

3. Target dir: The directory where all the certificates should be saved in.<br>
4. Mailing List: A CSV file in which each row consists of the name and email address of each participant.  
**Format**:<br>
name,email<br>
The name should match the name at field1 in participants.  
**Example**:<br>
Ajay Raj Nelapudi,ajayraj.cseanits@gmail.com<br>
Shiv Shankar Singh,shivshankarsingh@gmail.com<br><br>

### Outputs:
1. Certificates in .pdf format will be generated and saved at the dir given in target dir field.
2. Emails will be sent to the the address given in the mailing list.

The log files log usual activity and exceptions that rise during runtime. Please do not modify the log files in any manner.<br>
In case of any issues please email me a screenshot of the issue along with the main.log file.<br><br>

If you found my project useful, please star my repository.
