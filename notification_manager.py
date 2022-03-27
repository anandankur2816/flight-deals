import smtplib as smt
from api import *


def send_mail(message):
    with smt.SMTP("smtp.gmail.com", port=587) as conn:
        conn.starttls()
        conn.login(user=my_email, password=my_pass)
        conn.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=message
        )
        print("Mail sent")