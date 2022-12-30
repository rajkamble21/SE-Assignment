"""
    Test cases for otp program
    Author: Raj Kamble
"""

import math
import random
import smtplib

digits="0123456789ABCDEF"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
msg= otp
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("webapp212002@gmail.com", "rkqtoinehbgbtafg")
emailid = input("Enter your email: ")
s.sendmail('webapp212002@gmail.com',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")