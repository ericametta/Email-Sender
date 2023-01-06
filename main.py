import ssl
import smtplib
from email.message import EmailMessage


emailSender = 'ericamettaz@gmail.com'
emailPassword = '' #enter email password or import from password file
emailReceiver = 'em322721@ohio.edu'

emailSubject = "Your Daily Mail"
emailBody = """
Have a beautiful day. 
Next up: Nigerian Entertainment News.
Stay tuned.
"""

# create an instance of EmailMessage
em = EmailMessage()
em['From'] = emailSender
em['To'] = emailReceiver
em['subject'] = emailSubject
em.set_content(emailBody)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, emailPassword)
    smtp.sendmail(emailSender, emailReceiver, em.as_string())


