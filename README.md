# Certificate-Generator
Software brought to life based on the necessity to create and email 300 certificates to students, for the Spyry Workshop held at ANITS college.

INPUT FILES:
1. Template: An image in .png, .jpg, or .jpeg format, containing the certificate template upon which names will be written.<br>
2. Participants: A CSV file in which each row represents the data to be printed on each template.<br><br>
FORMAT:
field1,field2,field3,...,fieldN<br>
such that field1 is always the name of the candidate.<br><br>

EXAMPLE:<br>
Ajay Raj Nelapudi,IV/IV - CSE - A<br>
Shreya Gokavarapu,IV/IV - IT - A<br><br>

3. Target dir: The directory where all the certificates should be saved in.<br>
4. Mailing List: A CSV file in which each row consists of the name and email address of each participant.<br><br>
FORMAT:
name,email<br>
the name should match the name at field1 in participants<br>

EXAMPLE:
Ajay Raj Nelapudi,ajayraj.cseanits@gmail.com<br>
Shreya Gokavarapu,shreya.gokavarapu@gmail.com<br><br><br>

The log files log usual activity and exceptions that rise during runtime. Please do not modify the log files in any manner.<br>
In case of any issues please email me a screenshot of the issue along with the main.log file.<br><br>

If you found my project useful please star my repository. Thank you.
