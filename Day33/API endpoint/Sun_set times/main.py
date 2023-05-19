import requests
from datetime import datetime
#My latitude and my longitude of my location

My_LAT = 25.224300
MY_LONG = 84.990211


parameters = {
    "lat": My_LAT,
    "lng": MY_LONG
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunset)

time_now = datetime.now()

print(time_now)