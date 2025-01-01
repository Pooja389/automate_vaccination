import smtplib
import datetime as dt
import time
from dateutil.relativedelta import relativedelta


my_email = "my_email"
my_pass = "my_pass"

start_date = dt.datetime(2024,9,25).date()
def check():
    global start_date
    six_months_later = (start_date + relativedelta(months=6))
    today = dt.datetime.today().date()
    if today == six_months_later:
        start_date = six_months_later
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(my_email,my_pass)
            connection.sendmail(
                from_addr=my_email,
                to_addrs = my_email,
                msg=f'SUBJECT:lucy vaccination, it is the time to get vaccination for lucy'
            )
while True:
    check()
    time.sleep(86400)







