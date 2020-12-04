# coding=utf-8
import os
import smtplib, ssl
import gmail_cred as gc
from email.message import EmailMessage

critical = False
high = 60
too_high = 80

# At First we have to get the current CPU-Temperature with this defined function
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Now we convert our value into a float number
temp = float(getCPUtemperature())

# Check if the temperature is abouve 60°C (you can change this value, but it shouldn't be above 70)
if (temp > high):
    if temp > too_high:
        critical = True
        subject = "Critical warning! The temperature is: {}  , shutting down!".format(temp)
        body = "Critical warning! The temperature is: {} \n\n The Raspberry has been shut down !".format(temp)
    else:
        subject = "Warning! The temperature is: {} ".format(temp)
        body = "Warning! The temperature of your Raspberry Pi is: {} ".format(temp)

    # Login
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = gc.email
    msg['To'] = gc.remail

    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.starttls(context = context)
        smtp.login(msg['From'], gc.passwd)
        smtp.send_message(msg)

    # Critical, shut down the pi
    if critical:
        os.popen('sudo halt')
