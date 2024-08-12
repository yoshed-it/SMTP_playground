with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=test_email, password=test_password)
#     connection.sendmail(
#         from_addr=test_email, 
#         to_addrs='sauteboy@gmail.com', 
#         msg="Subject:SMTP Fuckery \n\n Fucking around with SMTP and some dummy emails.")