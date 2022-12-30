"""
    otp verification program with functional decomposition
    Author: Raj Kamble
"""

import math
import random
import smtplib
import re


owner_email = 'webapp212002@gmail.com'
owner_password = 'rkqtoinehbgbtafg'
otp_length = 4
user_email = None

#email validation
def email_validation(self, s):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat,s):
        return True
    return False

#otp generation
def generate_otp(self):
    digits="0123456789ABCDEF"
    OTP=""
    for i in range(self.otp_length):
        OTP+=digits[math.floor(random.random()*10)]
    return OTP

#sending email
def send_email(self, emailid, msg):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(self.owner_email, self.owner_password)
    s.sendmail(self.owner_email,emailid,msg)

#varifying otp
def verify_otp(self, OTP):
    a = input("Enter Your OTP >>: ")
    if a == OTP:
        print("Verified")
    else:
        print("Please Check your OTP again")




user_email = input("Enter Your Email >>: ")

if email_validation(user_email):
    OTP = generate_otp()
    msg = OTP + " is your OTP"
    send_email(user_email, msg)
    verify_otp(OTP)
else:
    print("Check your email")




    
   

