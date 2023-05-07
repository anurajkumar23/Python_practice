#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "anurajkumar6294@gmail.com"
MY_PASSWORD = "wctsrutapqizwcyu"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )





# import smtplib

# my_email = "anurajkumar6294@gmail.com"
# password = "wctsrutapqizwcyu"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="anurajsingh8507191590a@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email."
#                     )

# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# print(year)