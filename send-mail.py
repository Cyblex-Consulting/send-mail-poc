#!/usr/bin/python

import smtplib

########
# Config
########

sender_name = "Fake John Doe"
sender_email = 'jdoe@vulncorp.fr'

receiver_name = "Pentest Cyblex"
receiver_email = 'somewhere@cyblex-consulting.com'

smtp_ip = '1.2.3.4'
subject = "Impersonated email"

message = "This is an impersonated email"

###################
# Do not edit below
###################

data = "From: " + sender_name + " <" + sender_email + ">\n"
data += "To: " + receiver_name + " <" + receiver_email + ">\n"
data += "Subject: " + subject + "\n"
data += "\n"
data += message
data += "\n"

print("The message below will be sent:")
print("---------------------------------")
print(data)
print("---------------------------------")

try:
   smtpObj = smtplib.SMTP(smtp_ip)
   smtpObj.sendmail(sender_email, [receiver_email], data)
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
