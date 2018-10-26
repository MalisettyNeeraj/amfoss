import smtplib
import getpass
from email.mime.text import MIMEText as text 
user_id = input("Your gmail id \n")
user_password=getpass.getpass("ENTER UR PASS WORD \n")
receiver_id = input("Enter the sender email id \n")
subject = input("Subject of the mail \n")
message = input("Enter the message you want to send \n")
m=text(message)                  
m['subject'] = subject           
m['from'] = user_id                         
m['to'] = receiver_id
s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()      
s.login(user_id,user_password)
s.sendmail(user_id,receiver_id,m.as_string())   
s.quit()
print("Your message is sent.....")
