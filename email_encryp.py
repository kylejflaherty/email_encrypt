#Your Gmail account
import smtplib
 
#SMTP session for Gmail
s = smtplib.SMTP('smtp.gmail.com', 587)
 
#Start TLS for security
s.starttls()
 
#Your Gmail authentication
s.login("pluvi1044@gmail.com", "qytkffowpzljesrq")
 
#Message to be sent
message = "hello from python"
 
enc = input("\nEnter the message to encrypt:\n>>")
 
for i in range(0, len(enc)):
    message = message + chr(ord(enc[i]) - 4)
print(message)
 
#Send the mail
s.sendmail("pluvi1044@gmail.com", "kylejflaherty@gmail.com", message)
 
#Terminate
s.quit()