import smtplib
import datetime as dt
import random

my_email = "iruci.coleccion@gmail.com"
password = "Trang123()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0: #Monday
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("stmp.gmail.com") as connection:
         connection.starttls()
         connection.login(user=my_email, password=password)
         connection.sendmail(
             from_addr=my_email,
             to_addrs="dothuytrang2312@gmail.com",
             msg=f"Subject: Monday Motivation\n\n{quote}."
     )




