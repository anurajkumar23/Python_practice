import smtplib

my_email = "anurajkumar6294@gmail.com"
password = "wctsrutapqizwcyu"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="anurajsingh8507191590a@gmail.com",
                        msg="Subject:Hello\n\nThis is the body of my email."
                        )

