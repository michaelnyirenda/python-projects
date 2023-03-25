import requests
from datetime import datetime
import smtplib
import time

MY_LAT =  # Your latitude
MY_LONG =  # Your longitude
MY_EMAIL = # Your email
MY_PASSWORD = # Your password

def is_iss_overhead():
    # Your position is within +5 or -5 degrees of the ISS position.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if -5 < abs(iss_latitude - MY_LAT) < 5 and -5 < abs(iss_longitude - MY_LONG) < 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
        # Then send me an email to tell me to look up.
        
while True:       
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
                from_addr=MY_EMAIL, 
                to_addrs= # recipient email, 
                msg="Subject:ISS TRACKER\n\ngo outside. the international space station is above you."
                )
    time.sleep(60)










    