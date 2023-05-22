import requests
from datetime import datetime
import smtplib
import time
#My latitude and my longitude of my location

MY_EMAIL= "anurajkumar6294@gmail.com"
MY_PASSWORD = ""
My_LAT = 23.249100
MY_LONG = 87.869400

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude =float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)
    print(iss_position)

    #Your position is within +5 or -5 degrees of the iss position.
    if My_LAT-5 <= iss_latitude <= My_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    
def is_night():
    parameters = {
        "lat": My_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now<= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up👆\n\nThe ISS is above you in the Sky"
            )

