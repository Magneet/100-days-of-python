import smtplib
connection = smtplib.SMTP("smtpserver")
connection.starttls()
connection.login(user="user", password = "password")
connection.sendmail(from_addr="emailadd",to_addrs="otheremail",msg="Subject:gfgfdgdf\n\nBody f the email")
connection.close()